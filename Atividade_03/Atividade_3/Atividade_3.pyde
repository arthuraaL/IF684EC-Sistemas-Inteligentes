from collections import deque
from graph import Graph
from utils import BFS, UCS, Greedy, A_star, heuristic, make_grid, make_horizontal_walls, make_vertical_walls, make_sand, make_water
from agent import Agent

k = 0

def setup():
    global grid, cols, rows, agent, a_star, goal, start ##########TESTE##########
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
    start.wall = False
    goal = grid[int(random(0, cols-1))][int(random(0, rows-1))]
    goal.wall = False
    a_star = A_star(start, grid) ##########TEST###########
    agent = Agent(start.column, start.row)

    
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    make_sand(grid)
    make_water(grid)
    
# draw == while not frontier.empty()
def draw():
    delay(25)
    global rows, cols, grid, agent, a_star, k, h_wall, goal, start ######TESTE#######
    start.wall = False
    goal.wall = False
    came_from = dict()
    w = width / cols
    h = height / rows
        
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
 

#    if bfs.is_finish is False:
#        came_from = bfs(goal)
    if a_star.is_finished is False: ##########TEST###########
        came_from = a_star(goal) ##########TEST###########
    else:
#       path = bfs.reconstruct_path(came_from, goal)
        path = a_star.reconstruct_path(came_from, goal) ##########TEST###########
        k += 1
        if k < len(path):
            agent.update(x=path[k].column, y=path[k].row)
        else:
            k = 0
           # bfs = BFS(start, grid)
            a_star = A_star(start, grid) ##########TEST###########
            # goal = grid[int(random(1, cols-1))][int(random(1, rows-1))]
            # start = grid[int(random(1, cols-1))][int(random(1, rows-1))]
            print('DONE')
            noLoop()
    agent.display(w, h)

        
            
