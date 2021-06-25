from collections import deque
from graph import Graph
from utils import BFS, make_grid

def setup():
    global grid, cols, rows, frontier, came_from
    # Initializing a queue
    frontier = deque()
    came_from = dict()
    size(400, 400)
    rows = 20
    cols = 20
    w = width / cols
    h = height / rows
    grid = make_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Graph(j, i, w, h, 0)        

    for i in range(rows):
        for j in range(cols):
            grid[i][j].add_neighbors(grid)
    
    frontier.append(grid[0][0])
    came_from[grid[0][0]] = None
    

# draw == while not frontier.empty()
def draw():
    global rows, cols, grid, frontier, came_from        
    goal = grid[int(random(1, cols-1))][int(random(1, rows-1))]
    
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
    
    for i in came_from:
        strokeWeight(1)
        i.display(0)
    
    for i in frontier:
        strokeWeight(2)
        i.display(color(0,0,150))
    
    
    BFS(frontier, came_from, goal)

            
