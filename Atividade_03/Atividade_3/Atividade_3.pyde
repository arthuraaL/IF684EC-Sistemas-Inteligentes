from collections import deque
from graph import Graph
from utils import heuristic, make_grid, terrain_generator
from search import BFS, UCS, Greedy, A_star, DFS
from agent import Agent
from food import Food

k = 0
first_loop = True

def setup():
    global grid, cols, rows, agent, a_star, goal, start, food, bfs, a_star, ucs, greedy, dfs, first_loop
    # settings
    size(400, 400)
    rows = 20
    cols = 20
    w = width / cols
    h = height / rows
    # create a grid
    grid = make_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Graph(j, i, w, h, 0)        

    # adding neighbors for each element in the Graph
    for i in range(rows):
        for j in range(cols):
            grid[i][j].add_neighbors(grid)
    
    
        


    # setting start and goal
    start = grid[0][0]
    start.is_start = True
    goal = grid[int(random(0, cols-1))][int(random(0, rows-1))]
    goal.is_goal = True
    food = Food(goal)
    
    # create an object
    # a_star = A_star(start, grid)
    dfs = DFS(start, grid)

    # create the agent and a food
    agent = Agent(start.center)
    
    # obstacles, water, and sand
    terrain_generator(grid)
        
# draw == while not frontier.empty()
def draw():
    delay(100)
    global rows, cols, grid, agent, k, goal, start, food, bfs, a_star, ucs, greedy, dfs, first_loop
    came_from = dict()
    w = width / cols
    h = height / rows
        
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
 

    if dfs.is_finished is False:
        came_from = dfs(food.position) 
    else:
        path = dfs.reconstruct_path(came_from, food.position)
        k += 1
        if k < len(path):
            agent.update(path[k].center)
        else:
            k = 0
            # food counter
            food.count += 1
            print('Food Counter = ' + str(food.count))
            first_loop = False
            start = goal
            start.wall = False
            goal = grid[int(random(1, cols-1))][int(random(1, rows-1))]
            goal.wall = False
            # create an object
            dfs = DFS(start, grid)
            # create the agent and a food
            agent = Agent(start.center)    
            # update the food position
            food.update(goal)
            redraw()
    agent.display(w, h)
    food.display(w, h)
