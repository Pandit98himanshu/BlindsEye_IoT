#Credits: https://youtu.be/1LCb1PVqzeY

import cv2
from geopy.geocoders import Nominatim
from get_address import *
from upload_to_cloud import *
from get_datetime import *
from get_ipaddress import *
from create_bounding_boxes import *
from text_to_speech import *
from extract_info import *
from connect_to_cloud import *
from load_all_object_names import *

#Connecting to Mongodb cloud
collection=connect_to_cloud()

#Load YOLO Algorithm
net=cv2.dnn.readNet("yolov4-tiny.weights","yolov4-tiny.cfg")

#To load all objects that have to be detected
classes=load_all_object_names()

#Loading the Video
cap=cv2.VideoCapture(0) #openCV considers "0" as webcam

#Colors of bounding boxes
colors=np.random.uniform(0, 255, size=(len(classes), 3))

while True:
    #Extract info from raw image frame
    img, height, width, layerOutputs = extract_info_from_image(cap, net)
    
    boxes=[]            #bounding boxes
    confidences=[]      #confidences
    class_ids=[]        #predicted classes

    #Extract all informations from identified objects
    extract_info_from_layers(layerOutputs, boxes, confidences, class_ids, height, width)

    #Removes redundant boxes and keeping only boxes with high scores
    indexes=cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    #Pass all paramaters to show on the output video
    if len(indexes)>0:
        for i in indexes.flatten():
            #Creating bounding boxes
            label, confidence = create_bounding_boxes(i, img, boxes, classes, class_ids, confidences, colors)

            #Convert identified objects into speech format and play
            text_to_speech(label)
            
            #Get timestamp
            timestamp=get_datetime()

            #Get the address info
            address=get_address()

            #Get IP Address
            ip_address=get_ipaddress()
            
            #Uploading identified objects to the cloud
            upload_to_cloud(collection, ip_address, timestamp, label, confidence, address['display_name'])


    cv2.imshow("Output",img)
    key=cv2.waitKey(1)
    #Press esc key to stop the program
    if key==27:
        break
    
#Release camera
cap.release()
#Close all output windows
cv2.destroyAllWindows()
