def upload_to_cloud(collection, ip_address, timestamp, label, confidence, address):
    #Uploading paramenters to the Mongodb cloud
    post = { "ip_address" : ip_address, "timestamp" : timestamp, "label" : label, "confidence" : confidence, "address" : address}
    collection.insert_one(post)   
