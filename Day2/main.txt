def clients_feedback():
	ratings_dict = {}
	sum = 0
	count = 0
	print_comment = 2 
	## print ratings mean and some reviews
	print("     Ratings")
	print("-------------------")
	with open("ratings.txt") as f:
		for line in f:
			(rating, comment) = line.split('-')
			ratings_dict[rating] = comment
			if print_comment > 0:
				print(f"\n{line}")
				print_comment -=1
			
		for rating in ratings_dict:
			sum += int(rating)
			count +=1 
		print(f"\nThe mean of the ratings is: {sum/count}\n")
	# sort propositions by demand and print
	props_dict = {}
	with open("suggestions.txt") as f:
		for line in f:
			prop = line
			if prop in props_dict:
				props_dict[prop]+=1
			else:
				props_dict[prop] = 1
	sort_props = sorted(props_dict.items(),key=lambda x:x[1], reverse=True)
	print("\nPropositions sorted by demand:\n")
	print("Number of propositions        Item ")
	print("-----------------------       -----")
	for key,value in sort_props:
		print(f"        {value}                      {key}")



def purchase_history():
	history_dict = {}
	with open("purchases.txt") as f:
		for line in f:
			print(f"{line}")
			(item, times) = line.split('-')
			if item in history_dict:
				history_dict[item] += int(times)
			else:
				history_dict[item] = int(times)
	sort_history = sorted(history_dict.items(),key=lambda x:x[1], reverse=True)
	print(sort_history)
	print("\n  Purchase History:")
	print("-----------------------\n")
	print("Times purchased         Item ")
	print("-----------------       -----")
	for key,value in sort_history:
		print(f"        {value}               {key}")
	print("\n You should buy:")
	for key,value in sort_history:
		if value>5:
			print(f"- {key}")
			
def print_items():
	print("\n{:<15} {:<8} {:<3} {:<15} {:<8} {:<3} {:<15} {:<8}{:<3}".format('Item','Price','|','Item','Price','|','Item','Price','|'),end='')
	print("\n----------------------------------------------------------------------------------")
	items_dict = {}
	with open("items.txt") as f:
		for line in f:
		   (key, val) = line.split('-')
		   items_dict[key] = int(val)
	count=0
	for key in items_dict:
		print("{:<15} {:<8} {:<3}".format(f'{key}',f'{items_dict[key]}','|'),end='')
		count+=1
		if count >= 3:
			print("\n",end='')
			count = 0
			

		
	
		
# create a dictionary with items and their price
mode = input("Hello, are costumer or manager?\n$ ")
if mode == 'costumer':
	print_items()
	items_dict = {}
	with open("items.txt") as f:
		for line in f:
		   (key, val) = line.split('-')
		   items_dict[key] = int(val)

	#create dictionary for purchase	   
	purchase_dict = {}
	sum = 0
	end  = False
	print("Hello,")
	while end == False:
		new_item = input("what item would you like to purchase?\n$ ")
		quantity = input("How many would you like to purchase?\n$ ")
		purchase_dict[f"{new_item}"] = int(quantity)
		answer = input("would you like to purchase something else? (yes/no)\n$ ")
		if answer == 'yes': 
			continue
		else:
			end = True

	#calculate total		
	for item in purchase_dict:
		sum += (items_dict[item]*purchase_dict[item])

	#print result
	print("\n\nItem            Amount          Price")
	print("-----           ------          ------")
	for item in purchase_dict:
		print(f"{item}           {purchase_dict[item]}               {items_dict[item]*purchase_dict[item]}")
	print("-------------------------------------")
	print(f"Your total is:                    {sum}")

	with open("purchases.txt","a") as purchases:
		for item in purchase_dict:
			purchases.write(f"{item}-{purchase_dict[item]}")
			purchases.write("\n")
			
	# with open("purchases.txt","r") as purchases:
		# content = purchases.read()
	# print(content)

	suggestions = open("suggestions.txt","a")
	ratings = open("ratings.txt","a")
	ans = input("\nWould you like  to submit a review of the supermarket? (yes/no)\n$ ")
	if ans == 'yes':
		prop = input("\nWould you like to propose a new item? (yes/no)\n$ ")
		if prop == 'yes':
			con = True
			while con == True:
				item_prop = input("\nWhat item would you like to propose?\n$ ")
				suggestions.write(f"{item_prop}")
				suggestions.write("\n")
				again = input("\nWould you like to propose another item? (yes/no)\n$ ")
				if again == 'yes':
					continue
				elif again == 'no':
					con == False
					break
					
		rating = int(input("How much would you rate the supermarket from 1 to 5?\n$ "))
		ratings.write(f"{rating}-")
								
		comment = input("Tell us your review on the supermarket\n$ ")
		ratings.write(f"{comment}")
		ratings.write("\n")

		print("\nThank you for your time!")
	print("\nSee you next time!")
	suggestions.close()
	ratings.close()
elif mode == 'manager':
	print("Would you like to:\n(1) Print purchase history\n(2) Print ratings and item suggestions")
	type = input("$ ")
	if type == '1':
		purchase_history()
	elif type == '2':
		clients_feedback()


		
	

		
	
	

	