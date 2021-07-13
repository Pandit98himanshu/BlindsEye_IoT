#Load all object names which we have to be detected
def load_all_object_names():
    classes=[]
    with open("coco.names","r") as f:
        classes=f.read().splitlines()
        return classes
