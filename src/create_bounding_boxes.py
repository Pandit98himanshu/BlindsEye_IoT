import cv2

#Font of parameters
font=cv2.FONT_HERSHEY_PLAIN

def create_bounding_boxes(i, img, boxes, classes, class_ids, confidences, colors):
    x,y,w,h=boxes[i]
    label=str(classes[class_ids[i]])
    confidence=str(round(confidences[i],2))
    color=colors[i]
    #Creating bounding boxes
    cv2.rectangle(img,(x,y),(x+w, y+h),color,2)
    #Adding label & confidence over bounding boxes
    cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)    
    return label, confidence
