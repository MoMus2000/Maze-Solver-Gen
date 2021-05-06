import pygame
import random
import time

pygame.init() #initialize pygame


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0, 128, 0)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
SOME = (233,45,34)


solution = {}




size = (600,600)

screen = pygame.display.set_mode(size)

screen.fill((150,65,233))

pygame.display.set_caption(":))))))))))))))))")

done = False

clock = pygame.time.Clock()


width = 20 # Size of the square being made on screen

rows = int(size[0]/width)
cols = int(size[1]/width)

stack = [] # Used for backtracking


#We create a cell Class as the grid contains cell objects

class Cell():

	def __init__(self,x,y):
		width = 20
		self.x = x*width
		self.y = y*width

		self.visited = False
		# self.current = False


		self.walls = [True,True,True,True] # To create the cell walls

		 # Selecting next cell to move to

		self.top = 0
		self.right = 0
		self.bottom = 0
		self.left = 0

		self.next_cell = 0


	def draw(self):
		colors = [RED,BLUE,GREEN,INDIGO,VIOLET,ORANGE,YELLOW]
		# if self.current:
		# 	pygame.draw.rect(screen,WHITE,(self.x,self.y,width,width))
		
		if self.walls[0]:
			pygame.draw.line(screen,BLACK,(self.x,self.y),((self.x + width),self.y),5) # top
		if self.walls[1]:
			pygame.draw.line(screen,BLACK,((self.x + width),self.y),((self.x + width),(self.y + width)),5) # right
		if self.walls[2]:
			pygame.draw.line(screen,BLACK,((self.x + width),(self.y + width)),(self.x,(self.y + width)),5) # bottom
		if self.walls[3]:
			pygame.draw.line(screen,BLACK,(self.x,(self.y + width)),(self.x,self.y),5) # left

		if self.visited:
			# colo = random.choice(colors)
			pygame.draw.rect(screen,VIOLET,(self.x,self.y,width,width))
	

	def check_neighbors(self):
		self.neighbors = []
		if(int(self.y/width) -1 >=0 ):
			self.top = grid[int(self.y/width)-1][int(self.x/width)]

		if(int(self.y/width)+1 <= cols -1):
			self.bottom = grid[int(self.y/width)+1][int(self.x/width)]

		if(int(self.x/width)+1 <= rows -1):
			self.right = grid[int(self.y/width)][int(self.x/width)+1]

		if(int(self.x/width)-1 >=0 ):
			self.left = grid[int(self.y/width)][int(self.x/width)-1]

		if(self.top !=0):
			if(self.top.visited == False):
				self.neighbors.append(self.top)

		if(self.right !=0):
			if(self.right.visited == False):
				self.neighbors.append(self.right)


		if(self.bottom !=0):
			if(self.bottom.visited == False):
				self.neighbors.append(self.bottom)

		if(self.left !=0):
			if(self.left.visited == False):
				self.neighbors.append(self.left)


		if(len(self.neighbors) > 0 ):
			self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
			return self.next_cell

		else:
			return False

	def check_neighbors_for_dfs(self):
		self.neighbors = []
		if(int(self.y/width) -1 >=0 and grid[int(self.y/width)][int(self.x/width)].walls[0] == False and grid[int(self.y/width)-1][int(self.x/width)].walls[2] == False):
			# print("HERE1")
			self.top = grids[int(self.y/width)-1][int(self.x/width)]

		if(int(self.y/width)+1 <= cols -1 and grid[int(self.y/width)][int(self.x/width)].walls[2] == False and grid[int(self.y/width)+1][int(self.x/width)].walls[0] == False):
			# print("HERE1")
			self.bottom = grids[int(self.y/width)+1][int(self.x/width)]

		if(int(self.x/width)+1 <= rows -1 and grid[int(self.y/width)][int(self.x/width)].walls[1] == False and grid[int(self.y/width)][int(self.x/width)+1].walls[3] == False):
			# print("HERE2")
			self.right = grids[int(self.y/width)][int(self.x/width)+1]

		if(int(self.x/width)-1 >=0 and grid[int(self.y/width)][int(self.x/width)].walls[3] == False and grid[int(self.y/width)][int(self.x/width)-1].walls[1] == False):
			# print("HERE3")
			self.left = grids[int(self.y/width)][int(self.x/width)-1]

		if(self.top !=0):
			if(self.top.visited == False):
				# print("HERE TOP")
				self.neighbors.append(self.top)

		if(self.right !=0):
			if(self.right.visited == False):
				# print("HERE RIGHT")
				self.neighbors.append(self.right)


		if(self.bottom !=0):
			if(self.bottom.visited == False):
				# print("HERE BOTTOM")
				self.neighbors.append(self.bottom)

		if(self.left !=0):
			if(self.left.visited == False):
				# print("HERE LEFT")
				self.neighbors.append(self.left)

		print(self.neighbors)

		if(len(self.neighbors) >0):
			return self.neighbors

		else:
			return False

	def highlight(self):
		pygame.draw.rect(screen,SOME,(self.x,self.y,width,width))





def remove_walls(current_cell,next_cell):
	x = int(current_cell.x/width) - int(next_cell.x/width)
	y = int(current_cell.y/width) - int(next_cell.y/width)
	if x == -1: # right of current
		current_cell.walls[1] = False
		next_cell.walls[3] = False
	elif x == 1: # left of current
		current_cell.walls[3] = False
		next_cell.walls[1] = False
	elif y == -1: # bottom of current
		current_cell.walls[2] = False
		next_cell.walls[0] = False
	elif y == 1: # top of current
		current_cell.walls[0] = False
		next_cell.walls[2] = False



grids = []


def dfs():
	stack = []
	solution = []
	for y in range(rows):
		grids.append([])
		for x in range(cols):
			grids[y].append(Cell(x,y))
	start_node = grids[0][0]
	print(start_node.check_neighbors_for_dfs())
	# print(start_node)
	end_node = grids[len(grids)-1][len(grids)-1]

	stack.append(start_node)

	while(len(stack) >0 ):

		curr = stack.pop()

		solution.append(curr)

		if(curr == grids[len(grids)-1][len(grids)-1]):
			solution.append(grids[len(grids)-1][len(grids)-1])
			return solution
			
		elif(curr.visited):
			continue


		curr.visited = True


		neighbors = curr.check_neighbors_for_dfs()
		if(neighbors != False):
			for nei in neighbors:
				stack.append(nei)
		else:
			stack.pop()
				# nei.visited = True

	return []


	# print(start_node.x, start_node.y)
	# print(end_node.x,end_node.y)

	# stack.append(start_node)
	# start_node.visited = True
	# while(len(stack) > 0):
	# 	curr = stack.pop()
	# 	if(curr == end_node):
	# 		break
	# 	else:
	# 		neighbors = curr.check_neighbors_for_dfs()
	# 		if(neighbors != False):
	# 			for nei in neighbors:
	# 				if(nei.visited == False):
	# 					stack.append(nei)
	# 		curr.visited = True

	return solution

	


grid = []

for y in range(rows):
	grid.append([])
	for x in range(cols):
		grid[y].append(Cell(x,y))

# print(len(grid))
# print(len(grid[0]))
current_cell = grid[0][0]
next_cell = None

visited_list = []
while not done:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			done = True

	# font = pygame.font.Font(None, 200)
	# fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
	# screen.blit(fps, (200, 200))
	# screen.fill(WHITE)

	for y in range(rows):
		for x in range(cols):
			# grid[y][x].walls[0] = False 
			# grid[y][x].walls[2] = False 
			# grid[y][x].walls[3] = False 
			# print(grid[y][x])
			grid[y][x].draw()

	current_cell.visited = True
	current_cell.highlight()	

	next_cell = current_cell.check_neighbors()
	
	if next_cell != False:
		next_cell.visited = True
		stack.append(current_cell)
		visited_list.append((current_cell.x,current_cell.y))
		remove_walls(current_cell,next_cell)
		current_cell = next_cell
		# current_cell.current = False

	
	elif(len(stack) > 0):
		current_cell = stack.pop()


	elif(len(stack) == 0):
		x = dfs()
		print(x[0].x)
		container = []
		for val in x:
			if(val not in container):
				x_val = val.x
				y_val = val.y
				container.append((x_val,y_val))
		for objects in container:
			ob = objects
			pygame.draw.rect(screen,GREEN,(ob[0],ob[1],int(width/2),int(width/2)))
			clock.tick(20)
			pygame.display.flip()

		pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))
		screen.blit(pause_text, (100, 100))


		# print(x)
		
		# visited_list.pop()
	# 	stack.append(current_cell)
		
		# remove_walls(current_cell,next_cell)
		
		# current_cell.current = False
		
		# current_cell = next_cell
	
	pygame.display.flip()
	
	clock.tick(256)

pygame.quit()











