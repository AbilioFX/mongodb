from pymongo import MongoClient as MC


myclient = MC("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
"""
mydict = {"name": "John","address": "Highway 37"}
x = mycol.insert_one(mydict)
print(x)
insemydict = {}
insemydict["name"] = "Peter"
insemydict["address"] = "Lowerstreet 27"
y = mycol.insert_one(insemydict)
print(y.inserted_id)
"""
mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]
newx = mycol.insert_many(mylist)
newy = mycol.find()
for i in newy:
    print("newx:", i)
"""
print(newx.inserted_ids)

mylist2 = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x2 = mycol.insert_many(mylist2)
print(x2.inserted_ids)

item = mycol.find_one()
print(item)


for i in mycol.find():
    print(i)

for j in mycol.find({}, {"_id":0, "name": 1, "address": 1}):
    print(j)


myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)
for i in mydoc:
    print("Park Lane query respones: ", i)

myquery2 = {"address": {"$gt":"S"}}
mydoc2 = mycol.find(myquery2)
for i in mydoc2:
    print("Address greater than S: ", i)


myquery3 = { "address": { "$regex": "^S" } }
mydoc3 = mycol.find(myquery3)
for x in mydoc3:
    print(x)
"""