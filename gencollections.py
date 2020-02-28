#!gencollections.py
__doc__ = """Script for CiTi MongoDB and pymongo.
"""
try: 
	from pymongo import MongoClient
except ImportError:
	print("Pymongo not installed correctedly...\nPlease run <python -m pip install pymongo> before executing htis script.")
from pprint import pprint
from sprintfuncs import *
from time import sleep

confirm = ["y", "Y", "yes", "ok"]

cost_list = [16,18,12,18,18,16,18,13,13,1,16,16,13,20,40,35,44,42,36,4,20,5,3,6,5,5,6,3,2,3,3,5,3,6,0.5,5,5,3.5,1,5,2.5,6,22,13,16,18,16,30,32,15,18,23,25,35,13, 15]

selling_list = calc(cost_list )
quantity_bought = calc(cost_list, kw="quantity_bought" )
quantity_sold = calc(cost_list, kw="quantity_sold")
profit_list = profit(cost_list, selling_list, quantity_bought, quantity_sold) 




col_struct= {
			 "cooldrinks": ["Jive", "Coca-cola", "Twizza", "Mountain_dew", "Pepsi", "Fanta", "Sprite"],
			 "pies": ["Pepper_steak", "Mushroom_&_chicken", "Steak_&_kidney", "Feta_&_cheese", "Mutton_curry", "Chicken", "Burger"],
			 "cigarettes": ["Stuyvesant", "Rothmans", "Dunhill", "Kent", "Pall_Mall", "Benson&Hedges", "Ceasar"],
			 "chocolates": ["Lunch_bar", "Chomp", "Kit_kat", "Crunchie", "Bar_one", "Snickers", "Twix"],
			 "fruit": ["Apples", "Bananas", "Oranges", "kiwis", "Pears", "Mangoes", "Apricots"],
			 "chips":["Doritos","Simba", "Fritos", "NikNaks", "Lays", "Ghost_Pops", "Big_Korn_Bites"],
			 "sweets":["Eclairs", "Jelly_tots", "Smarties", "Chappies", "Jaw_breakers", "Fizzers", "Wilson_toffees"],
			 "veggies": ["Spinach", "Cauliflower", "Pumpkin", "Cucumber", "Lettuce", "Potatoes", "Carrots"]
			}

dict_struct= {
			  "_id": None, 
 			  "product_name": ["Jive", "Coca-cola", "Twizza", "Mountain_dew", "Pepsi", "Fanta", "Sprite", "Pepper_steak", "Mushroom_&_chicken", "Steak_&_kidney", "Feta_&_cheese", "Mutton_curry", "Chicken", "Burger", "Stuyvesant", "Rothmans", "Dunhill", "Kent", "Pall_Mall", "Benson&Hedges", "Ceasar", "Lunch_bar", "Chomp", "Kit_kat", "Crunchie", "Bar_one", "Snickers", "Twix", "Apples", "Bananas", "Oranges", "kiwis", "Pears", "Mangoes", "Apricots", "Doritos","Simba", "Fritos", "NikNaks", "Lays", "Ghost_Pops", "Big_Korn_Bites", "Eclairs", "Jelly_tots", "Smarties", "Chappies", "Jaw_breakers", "Fizzers", "Wilson_toffees", "Spinach", "Cauliflower", "Pumpkin", "Cucumber", "Lettuce", "Potatoes", "Carrots"], 
			  "cost_price": cost_list,#[16,18,12,18,18,16,18,13,13,1,16,16,13,20,40,35,44,42,36,4,20,5,3,6,5,5,6,3,2,3,3,5,3,6,0.5,5,5,3.5,1,5,2.5,6,22,13,16,18,16,30,32,15,18,23,25,35,13, 15], 
			  "selling_price": selling_list, 
			  "quantity_bought": quantity_bought, 
			  "quantity_sold": quantity_sold, 
			  "profit": profit_list
			  }
#pprint(dict_struct)	 
#pprint(dict_struct)

conn=MongoClient('mongodb+srv://abilioX:C0nstruct.123@cluster0-cd3i4.mongodb.net/test?retryWrites=true&w=majority', )
with conn:
	#create and reference a database
	db = conn["Data_Tracker"]
	#create and reference to collections
	top3 = db["Top_3"]
	mycol = db["Storage"]
	mycols = map(gen_cols, list(col_struct.keys()), db)
	[pprint(mycols)]
	#Insert documents
	insert_d = gen_docs(dict_struct, col_struct)
	print("Dict collection")
	pprint(insert_d)
	#pprint(insert_d)
	mycol.insert_many(insert_d)
	#Updates to 'Storage' collection. 
	mycol.update_many({}, {"$set": gen_barcode()})
	#Extractions/Sortings of documents in database
	fav_3 = mycol.find(limit=3).sort("profit", -1)
	#Insertions of top three products in 'Top_3' collection.
	favs = []
	[favs.append(fav) for fav in fav_3]
	top3.insert_many(favs)
	#Deletion of documents
	profitable = top3.find_one()
	pprint(profitable)
	value = profitable["profit"]
	print(value)
	#[print("Profitable item", p) for p in profitable]
	ans = input("Delete two documents from 'Top_3' collection? ")
	if ans in confirm:
		try:
			del_query = {"profit": {"$lt": value}}
			print("Deleting.....5")
			sleep(5)
			top3.delete_many(del_query)
		except Exception as e:
			print(f"{e}")
	#Filtering and
	s = mycol.find({"selling_price": {"$gt": 20}}, limit=6).sort("selling_price", -1)
	print("Filtered documents from Storage collection ->")
	[pprint(i) for i in s]
	#Drop collection 
	print("Preparing to exit please wait a moment.....10")
	sleep(10)
	ans2 = input(f"Exit and delete database {db._Database__name}? ")
	if ans2 in confirm:
		try:
			conn.drop_database(db._Database__name)
		except Exception as e:
			print(f"{e}")
	else:
		print(f"Collections still conatined in database - '{db._Database__name}' are\n\n")
		[print(f"{i}") for i in db.list_collection_names()]
"""

def opdb():
	db = conn["Data_Tracker2"]
	#create and reference to collections
	top3 = db["Top_3"]
	mycol = db["Storage"]
	mycols = map(gen_cols, list(col_struct.keys()), db)

@ContextManger
def run():
	try:
		db = conn["Data_Tracker2"]
		yield db
	except Exception as e:

	
"""
