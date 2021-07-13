import pymongo
from pymongo import MongoClient

def connect_to_cloud():
    #Connecting to Mongodb cloud
    cluster=MongoClient("mongodb+srv://SujoySeal:bKWb09V1uBbMMhJb@post-boxcluster-sujoy.i9ean.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #Assigning database
    db=cluster["FYP-Database"]
    #Assigning collection
    collection=db["Identified-Objects"]
    return collection
