import random
def board_draw(height, width,board):
    for x in range(height):
        print("  -------- " * width)
        print("|" +
              "|".join('{:{align}{width}}'.format(board[x][y].name ,align='^',width='10')
                       for y in range(width)) +
              "|")
    print("  -------- " * width)
	

class Object:
	def __init__(self):
		self.name = '*'
	
	def put_on_board(self,board,width,height):
		while(con == True):
			w = random.randint(0,width-1)
			if w == 0 or w==width-1:
				h= random.randint(0,height-1)
			else:
				h = 0
			if board[w,h].name == '*':
				board[w,h] = self
				con = False
			else:
				continue
	
				
"""
class Animal(Object):
	def __init__(self,name, size, speed):
		self.name = name
		self.size = size
		self.speed=speed
	

		
	
	def run(self,board)
	
	def eat(self,board)
	
	def got_eaten(self,board)
	
		
class Deer(Animal):

	def __init__(self,name,size,speed):
		super().__init__(self,'DEER',1,2):
		
	
	def print_animal(self):
		print("DEER")
		
		
class Lion(Animal):

	def __init__(self,size,speed):
		super().__init__(self,'LION',2,1):
	
	def print_animal(self):
		print("LION")	

class Food(Object):
	
	def __init__(self,name)
		self.name = name
		
	def put_on_board(self, board)
	
	def got_eaten(self,board)
	
class Leaf(Food):
	def __init__(self)
		super().__init__(self,'LEAF')
		
class Berries(Food):
	def __init__(self)
		super().__init__(self,'BERRIES')
"""
width, height = 7,8
print(width)
board = [[Object() for x in range(width)]for y in range(height)]
# board_draw(height+1,width+1,board)
for i in range(width-1):
	for j in range(height-1):
		print(f"{board[i][j].name} {i},{j} ",end='')
	print("\n")


