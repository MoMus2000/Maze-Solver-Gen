import pygame
import random
(width, height) = (200, 200)
screen = pygame.display.set_mode((width, height))

# pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, 10, 10))
# pygame.display.flip()

running = True

w, h = 201, 201;
visited = [[0 for x in range(w)] for y in range(h)] 


def valid_cell(x,y):
	return x>=0 and x <200 and y >=0 and y <200

def dfs(visited,  x,  y):
	visited[x][y] = 1
	pygame.draw.rect(screen,(255,255,255),pygame.Rect(x,y,1,1))
	pygame.display.flip()
	choice = []
	choice = [1,2,3,4]
	choice = random.choice(choice)
	print(choice)
	if(choice == 1 and visited[x+1][y] != 1):
		pygame.draw.line(screen,(255,0,0),(x,y,))
		dfs(visited,x+1,y)
	elif(choice == 2 and visited[x-1][y] != 1):
	 	dfs(visited,x-1,y)
	elif(choice == 3 and visited[x][y+1] != 1):
		dfs(visited,x,y+1)
	elif(choice == 4 and visited[x][y-1] != 1):
		dfs(visited,x,y-1)

	return

BLACK = (0,0,0)
grid =[]
def build_grid(x, y, cell_width=40):
    for n in range(20):
        x = 40
        y = y + 40
        for m in range(20):
            pygame.draw.line(screen, BLACK, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(screen, BLACK, [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(screen, BLACK, [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(screen, BLACK, [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            x = x + 40
            pygame.display.update()

build_grid(40,0,40)

while running:

	# clockobject = pygame.time.Clock()
	# clockobject.tick(20)

	for event in pygame.event.get():
		running = False
	# dfs(visited,50,50)
	# while True:
	# 	pass

	# for i in range(0,500):
	# 	for j in range(0,500):
	# 		pygame.draw.rect(screen,(255,255,255),pygame.Rect(i,j,10,10))
	# 		pygame.display.flip()









