############ex1
name = input("What is your name?")
print(f"Hello {name}!")

#---------------------------------------------------------------------------------------------------------------
############ex2
name1=input("what is the first user's name?")
len1=len(name1)
name2= input("and the second user's name?")
len2=len(name2)
if len1==len2:
	print("both of your names have the same length")
elif len1>len2:
	print(f"{name1}, your name is longer")
else:
	print(f"{name2}, your name is longer")
	
#---------------------------------------------------------------------------------------------------------------
############ex3
name = input("What's your name?")
name=name.lower()
if (name[0] == 'a') or (name[0] == 'e') or (name[0] == 'u') or (name[0] == 'i') or (name[0] == 'o'):
	print("Hello there")

#---------------------------------------------------------------------------------------------------------------
############ex4
name = input("Hello, what's your name?")
i = len(name)
i -=1
if name[i] == 'a' or name[i]=='e' or name[i]=='u' or name[i]=='o' or name[i]=='i':
	print("The last letter in your name is a vowel")
else:
	print("The last letter of your name is a consonant")

#---------------------------------------------------------------------------------------------------------------	
############ex5
x = int(input("Enter a number "))
y = int(input("Enter another number "))

print(f"The sum is: {x+y}")

#---------------------------------------------------------------------------------------------------------------
############ex6
str = input("Hello, I challenge you to write the longest sentence without any A\n")
len = 0
fail = False
for element in str:
	if element == 'A' or element == 'a':
		print("FAIL!")
		fail = True
		break
	elif element != ' ':
		len +=1
if fail==False:
	print(f"Nice, you wrote {len} letters")
	
#---------------------------------------------------------------------------------------------------------------
############ex7
name = input("Hello, enter your full name:\n")
count_space = 0
fail = False
for element in name:
	if element == ' ':
		count_space += 1
		if count_space > 1:
			fail = True
			break
		space = name.index(element)
	elif (ord(element)<65) or (ord(element)>90 and ord(element)<97) or (ord(element)>122):
		fail = True
		break
if fail == False:
	if ord(name[0])<65 or ord(name[0])>90 or ord(name[space+1])<65 or ord(name[space+1])>90:
		print("Invalid Name")
	else:
		print("Valid Name")
else:
	print("Invalid Name")

#---------------------------------------------------------------------------------------------------------------	
############ex8
str = input("enter a sentence:\n")
count_space=0
for element in str:
	if element == ' ':
		count_space+=1
print(f"There are {count_space+1} letters in this sentence")

#---------------------------------------------------------------------------------------------------------------
############ex9
str = input("Hello, Enter a string\n")
if len(str)<4:
	print("")
else:
	len=len(str)
	new= str[0]+str[1]+str[len-2]+str[len-1]
	print(new)

#---------------------------------------------------------------------------------------------------------------
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) 
# and then tell him how old he turnt/will turn this year.

date = input("What's your birthday in DD/MM/YYYY format?:\n")
year = int(date[6:10])
print(year)
print(f"This year you turnt/will turn {2020-year}")


#---------------------------------------------------------------------------------------------------------------
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) 
# and then tell him how old he is today.
year_today=2020
month_today=10
day_today=19
date = input("What's your birthday in DD/MM/YYYY format?:\n")
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])
if month > month_today or (month==month_today and day>day_today):
	year_today=2019

print(f"today you are {year_today-year}")


#---------------------------------------------------------------------------------------------------------------
# Write a program that counts the number of element for a list, 
# without the len function.

name=['Alex','Mike','Dylan','Yossi']
count=0
for element in name:
	count +=1
print(f"The length of the list is {count}")


#---------------------------------------------------------------------------------------------------------------
#Write a program that print every name that starts by ‘a’

name=['Alex','Mike','Dylan','yossi','Alan']
count = 0
for element in name: 
	if element[0] == 'A' or element[0] == 'a':
		count += 1
print(f"The number of names that start with 'A' is: {count}")
	

#---------------------------------------------------------------------------------------------------------------
# Write a Python program that prints all the numbers 
# from 0 to 10 except 3 and 6.

for i in range(10):
	if i!=3 and i!=6:
		print(i)


#---------------------------------------------------------------------------------------------------------------		
# You have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

# At the end, print the final list.

names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
copy = names.copy()
for element in names:
	age=int(input(f"{element}, How old are you?\n"))
	if age < 16:
		copy.remove(element)
		
print(copy)


#---------------------------------------------------------------------------------------------------------------
#Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

#(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

numbers = list(range(1, 1000001)) 
for element in numbers:
	print(element)


#---------------------------------------------------------------------------------------------------------------	
# Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers .

numbers = list(range(1, 1000001)) 
print(f"Max number is: {max(numbers)} \nMin numbers is: {min(numbers)}\nAnd the Sum is: {sum(numbers)}")


#---------------------------------------------------------------------------------------------------------------

# Create a board as following by using for loops:

    # X
    # XX
    # XXX
    # XXXX
    # XXXXX
    # XXXXXX
    # XXXXX
    # XXXX
    # XXX
    # XX
    # X
	
for i in range(1,7):
	for j in range(i):
		print("X",end ='')
	print("\n",end='')
for i in range(1,6):
	k=6-i
	for j in range(k):
		print("X",end ='')
	print("\n",end='')	
	

#---------------------------------------------------------------------------------------------------------------

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

list = []
for i in range(1,11):
	list.append(3*i)
for element in list: 
	print(element)

#---------------------------------------------------------------------------------------------------------------

# You have two lists, current_players and new_players, 
# use a while loop to transfer every player from new_players to current_players.
current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
length = len(new_players)
i=0
while i< length:
	current_players.append(new_players[i])
	i+=1
print(current_players)

#---------------------------------------------------------------------------------------------------------------