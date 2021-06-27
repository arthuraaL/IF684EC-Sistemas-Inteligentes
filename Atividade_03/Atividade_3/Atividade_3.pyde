from collections import deque
from graph import Graph
from utils import BFS, make_grid
from agent import Agent

def setup():
    global grid, cols, rows, agent, bfs
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
    
k = 0

# draw == while not frontier.empty()
def draw():
    delay(300)
    global rows, cols, grid, agent, bfs, k
    came_from = dict()
    w = width / cols
    h = height / rows
    goal = grid[5][6]
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
 

    if bfs.is_finish is False:
        came_from = bfs(goal)
    else:
        path = bfs.reconstruct_path(came_from, goal)
        k += 1
        if k < len(path):
            agent.update(x=path[k].column, y=path[k].row)
        else:
            print('DONE')
            noLoop()
    agent.display(w, h)

        
            
