#!sprintfuncs.py
from random import randint
from itertools import count #cycle
from pprint import pprint


__all__ = ["gen_barcode", 
		   "gen_id", 
		   "gmap", 
		   "map", 
		   "calc", 
		   "profit", 
		   "gen_cols",
		   "gen_docs"]
#Internal functions
def cat(struct1, struct2, p_name):
		check = struct1["product_name"].index(p_name) / 7
		l = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
		for i in l:
			while check < i or check >= 7.0:
				for k in struct2:
					if p_name in struct2[k]:
						p_cat = k
						return p_cat

def f(length):
	def decorator(func):
		def wrapper(*args, **dict_struct):
			for i in range(length):

				func(*args, **kwargs)

		return wrapper
	return decorator

#Functions for external use
def gen_barcode( start=0, end=9, length=10):
	l = []
	for i in range(length):
		l.append(str(randint(start, end)))

	barcode = "".join(l)
	
	return {"barcode": int(barcode)}

def gen_id(num=5):
	d = gen_barcode(length=num)
	return d["barcode"]

def gmap(func, iterable, db):
	"""Generator to loop through iterable calling func it's items."""
	for item in iterable:
		yield func(db, item)

def map(func, iterable, db):
	"""Pass function and iterable to gmap generator to return a list of results from applying func to items in iterables."""
	return list(gmap(func, iterable, db))

def calc(iterable:list, kw:str="selling") -> list:
	container = []
	for i in iterable:
		if kw == "selling":
			i = i + (i * 25 / 100)
			container.append(i)
		elif kw == "quantity_bought":
			i = i * 10
			container.append(i)
		elif kw == "quantity_sold":
			#Minus quater of cost
			i = (i * 10) - (i / 25)
			container.append(i)
		else:
			container.append(None) 

	return container

def profit(cost:list, selling:list, quantity_bought:list, quantity_sold:list, profit:list=[]) -> list:
	"""Calculates profit of each product and returns them as a list."""
	for c_price, s_price, q_bought, q_sold in zip(cost, selling, quantity_bought, quantity_sold):
		p = (s_price * q_sold) - (c_price * q_bought )
		profit.append(p)
	return profit

def gen_cols(db, colname):
	"""Generate collections from dict keys."""
	return db[colname]

def gen_docs(struct:dict, col_struct:dict)->list:
	"""Format product data in dict for inserting into databases' collection."""
	docs = []
	assert len(struct.keys()) == 7, f"Amount of 'Dict keys' not appropriate, need '7' --> {repr(struct)}"
	try:
		for i in struct:
			if i == "_id":
				continue
			for j in struct.values():
				if j == None:
					continue
				assert len(j), f"Amount of items in 'Dict values' not appropriate --> {repr(struct.values() ) }"
	except Exception as e:
		print(f"Error in {str(e)}")

	for (p_id, p_name, p_cost,p_selling,p_q_bought,p_q_sold,p_profit) in zip(count(),struct["product_name"],struct["cost_price"],struct["selling_price"],struct["quantity_bought"],struct["quantity_sold"],struct["profit"]):
		p_cat = cat(struct, col_struct, p_name)
		docs.append({"_id": p_id,
					 "category": f"{p_cat}",
 			   		 "product_name": f"{p_name}", 
			   	   	 "cost_price": p_cost, 
			   		 "selling_price": p_selling, 
			   	 	 "quantity_bought": p_q_bought, 
			   		 "quantity_sold": p_q_sold, 
			   		 "profit": p_profit})
	#pprint(docs)
	return docs 