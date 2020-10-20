import random
def print_matrix(matrix,size):
	for i in range(size):
		for j in range(size):
			print(f"{matrix[i][j]} ",end='')
		print("\n")

size =int(input("What's the size of the matrix?\n$ "))
matrix = [[0 for x in range(size)]for y in range(size)]
result = [[0 for x in range(size)]for y in range(size)]
for i in range(1,size-1):
	for j in range(1,size-1):
		matrix[i][j] = random.randint(0,1)
		result[i][j] = matrix[i][j]
print("Original matrix:")
print("------------------------")
print_matrix(result,size)

con = True
round = 0
while con == True:
	round +=1
	for i in range(1,size-1):
		for j in range(1,size-1):
			
				#count live neighbors
			count = 0
			for n in range(i-1,i+2):
				for m in range(j-1,j+2):
					if n == i and m==j:
						continue
					else:
						if matrix[n][m] == 1:
							count+=1
			if matrix[i][j] == 1:
				#Any live cell with fewer than two live neighbours dies, 
				#as if by underpopulation.
				if count < 2:
					result[i][j] =0
				#Any live cell with more than three live neighbours dies, 
				#as if by overpopulation.
				if count > 3:
					result[i][j] = 0
			elif matrix[i][j] ==0:
				#Any dead cell with exactly three live neighbours becomes a live cell, 
				#as if by reproduction.
				if count == 3:
					result[i][j] = 1
					
	for i in range(1,size-1):
		for j in range(1,size-1):
			matrix[i][j] = result[i][j]
	print("------------------------")
	print(f"     Round {round}")
	print("------------------------")
	print_matrix(result,size)
	again = input("\n Another round? (yes/no)\n$ ")
	if again == 'yes':
		continue
	elif again == 'no':
		con = False						
			