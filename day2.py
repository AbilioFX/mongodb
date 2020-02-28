from pymongo import MongoClient as mc

myclient = mc("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

"""
mydoc = mycol.find().sort("name")
for i in mydoc:
    print(i)

mydoc2 = mycol.find().sort("name", -1)
for i in mydoc2:
    print(i)

mydoc3 = mycol.find().sort("name", 1)
for i in mydoc3:
    print(i)    

myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)
for x in mycol.find():
    print("printing all:",x)

myquery2 = {"address": {"$regex": "^S"}}
mycol.delete_many(myquery2)
print(x.deleted_count, "document deleted")


x = mycol.delete_many({})
print(x.deleted_count, "documents deleted")

print(mycol["customers"])   

print(mycol)
if mycol.drop() == True:
    print("Successfully dropped...")
elif mycol.drop() == False:
    print("Unsuccessful...")


myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)
"""
myquery2 = {"address": {"$regex":"^S"}}
newvalues2 = {"$set": {"address": "Canyon 123"}}
mycol.update_many(myquery2, newvalues2)
for x in mycol.find(limit=5):
    print(x)