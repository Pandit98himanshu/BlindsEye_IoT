import cv2
import numpy as np

def extract_info_from_image(cap, net):
    #Capture each frames of the video file
    _, img=cap.read()
    #Capturing its height and width used to scale back to original file
    height,width,_=img.shape

    #Extracting features to detect objects
    blob=cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
                                                            #Inverting blue with red
                                                            #bgr->rgb

    #We need to pass the img_blob to the algorithm
    net.setInput(blob)

    output_layers_names=net.getUnconnectedOutLayersNames()
    layerOutputs=net.forward(output_layers_names)

    return img, height, width, layerOutputs


def extract_info_from_layers(layerOutputs, boxes, confidences, class_ids, height, width):
    #Extract all informations form the layers output
    for output in layerOutputs:
        #Extract information from each of the identified objects
        for detection in output:
            #Should contain 4 bounding boxes, or 85 parameters
            scores=detection[5:]            #First 4 parameters are locations(x, y, h, w) and 5th element is confidence
            #Get index having maximum scores
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            #If confidence is strong enough, get locations of those bounding boxes
            if confidence>0.5:
                center_x=int(detection[0]*width)
                center_y=int(detection[1]*height)
                w=int(detection[2]*width)
                h=int(detection[3]*height)

                x=int(center_x-w/2)
                y=int(center_y-h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
