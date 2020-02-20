from pymongo import MongoClient as MC


myclient = MC("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name": "John","address": "Highway 37"}
x = mycol.insert_one(mydict)
print(x)
insemydict = mydict
insemydict["name"] = "Peter"
insemydict["address"] = "Lowerstreet 27"
y = mycol.insert_one(insemydict)
print(y.inserted_id)