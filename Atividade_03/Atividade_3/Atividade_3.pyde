from collections import deque
from graph import Graph
from utils import BFS, make_grid
from agent import Agent

def setup():
    global grid, cols, rows, agent, bfs
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
    
    start = grid[0][0]
    bfs = BFS(start, grid)
    agent = Agent(start.column, start.row)
    

# draw == while not frontier.empty()
def draw():
    global rows, cols, grid, agent, bfs
    w = width / cols
    h = height / rows
    goal = grid[8][10]
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
 
    bfs(goal)
    agent.display(w, h)    
    # if b_flag:
    #     noLoop()    
    # agent.arrive(goal.center)
    # agent.update()
        
            
