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

for p_name in dict_struct["product_name"]:
	check = dict_struct["product_name"].index(p_name) / 7
	p_cat = ""
	if str(check) in ["0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0"]:
		for k in col_struct:
			if p_name in col_struct[k]:
				p_cat = k 

	print(p_cat)
	#print(check)