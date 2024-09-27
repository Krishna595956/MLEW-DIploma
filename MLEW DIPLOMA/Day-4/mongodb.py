from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://krishna:1234567890@diploma.1v5g6.mongodb.net/") #connecting to the cluster
database=cluster['diploma'] #Database selection
collection=database['krishna']  #collection selection

print("Database connected")

def InsertOne():
    collection.insert_one({
        "name":"Krishna",
        "email":"k@gmail.com",
        "mobile":"1234567890"
    })
    print("data inserted")
    return 

def InsertMany():
    collection.insert_many([
        {"name":"dict1"},
        {"name":"dict2"},
        {"name":"dict3"}
    ])
    return

def DeleteOne():
    collection.delete_one({"name":"Krishna"})
    print("document deleted")
    return

def DeleteMany():
    collection.delete_many({"name":"dict1"})
    print("Multiple records deleted")
    return

def Find():
    data=collection.find({"name":"dict3"})
    
    print(list(data))
    return
# Find()

def FindOne():
    data=collection.find_one({"name":"Krishna"})
    print(data)
    return
# FindOne()

def UpdateOne():
    collection.update_one({"name":"Krishna"},{"$set":{"email":"krishna@gmail.com"}})
    print("Record updated")
    return 
UpdateOne()