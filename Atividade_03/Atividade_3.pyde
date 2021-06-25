from collections import deque
from graph import Graph

def setup():
    global grid, cols, rows, frontier, explored
    # Initializing a queue
    frontier = deque()
    explored = list()
    size(400, 400)
    rows = 10
    cols = 10
    w = width / cols
    h = height / rows
    grid = make_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Graph(j, i, w, h, 0)
    
    frontier.append(grid[5][5])            

    for i in range(rows):
        for j in range(cols):
            grid[i][j].add_neighbors(grid)
    
    

# draw == while not frontier.empty()
def draw():
    global rows, cols, grid, frontier, explored    
        # current = frontier.popleft()
        # explored.append(current)        
    # display grid to debug
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)
    
    for node in frontier:
        strokeWeight(2)
        node.display(color(0, 0, 255))
        for neighbor in node.neighbors:
            neighbor.display(color(0, 255, 0), True)        
            
def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]
