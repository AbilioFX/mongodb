from pymongo import MongoClient as MC 
#import pandas as pd
from passgen import main


doc_list = [{"_id": 0, 
			 "brand_name": "name", 
			 "cost_price": 0.0, 
			 "selling_price": 0.0, 
			 "quantity_bought": 0, 
			 "quantity_sold": 0, 
			 "profit": 0.0},
			{"_id" : 1, 
			 "brand_name": "name", 
			 "cost_price": 0.0, 
			 "selling_price": 0.0, 
			 "quantity_bought": 0, 
			 "quantity_sold": 0, 
			 "profit": 0.0},
			{"_id": 3, 
			 "brand_name": "name", 
			 "cost_price": 0.0, 
			 "selling_price": 0.0, 
			 "quantity_bought": 0, 
			 "quantity_sold": 0, 
			 "profit": 0.0},
			{"_id": 4, 
			 "brand_name": "name", 
			 "cost_price": 0.0, 
			 "selling_price": 0.0, 
			 "quantity_bought": 0, 
			 "quantity_sold": 0, 
			 "profit": 0.0},
			{"_id": 5, 
			 "brand_name": "name", 
			 "cost_price": 0.0, 
			 "selling_price": 0.0, 
			 "quantity_bought": 0, 
			 "quantity_sold": 0, 
			 "profit": 0.0}]

doc = {"barcode": main(7)}

col_list = ["chips",
			"chocolates",
			"pies",
			"fruit",
			"cooldrinks",
			"cigarettes",
			"sweets"]

	

def create_collections(db, col_names=col_list):
	for col_name in col_names:
		db[col_name]

		
if __name__ == '__main__':
	import sys
	dbname = input("Enter name for database: ")
	
	if "-local" in sys.argv:
		conn = MC("mongodb://localhost:27017")
		
		with conn:
			
			db = conn[dbname]
			
			create_collections(db)
			
			for i in range(len(col_list)):
				try:
					cur_col = db[col_list[i]]

					cur_col.insert_many(doc_list)
					cur_col.update_many({}, {"$set": doc})
				except Exception as e:
					print(f"Insertions or Updates error -> {e}")

			
			for collection in db.list_collection_names():
				documents = db[collection].find()
				print(f"--> {collection}\n{'-'*20}\n\n")
				for doc in documents:
					print(f"{doc}\n{'='*20}\n\n")

	elif "-remote" in sys.argv:
		conn = MC("mongodb+srv://abilioX:C0nstruct.123@cluster0-cd3i4.mongodb.net/test?retryWrites=true&w=majority")
		
		with conn:
			
			db = conn[dbname]
			
			create_collections(db)
			
			for i in range(len(col_list)):
				try:
					cur_col = db[col_list[i]]

					cur_col.insert_many(doc_list)
					cur_col.update_many({}, {"$set": doc})
				except Exception as e:
					print(f"Insertions or Updates error -> {e}")
			
			
			
			for collection in collections:
				documents = db[collection].find()
				print(f"--> {collection}\n{'-'*20}\n\n")
				for doc in documents:
					print(f"{doc}\n{'='*20}\n\n")