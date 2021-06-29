from collections import deque
from graph import Graph
from utils import heuristic, make_grid, terrain_generator
from search import Search
from agent import Agent
from food import Food
import argparse

k = 0
search_type = 'a_star'            # bfs, dfs, ucs, greedy, a_star
bricks = 7 # wall size

def setup():
    global grid, cols, rows, agent, goal, start, food, search
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
    start = grid[int(random(0, cols-1))][int(random(0, rows-1))]
    start.is_start = True
    start.wall = False
    goal = grid[int(random(0, cols-1))][int(random(0, rows-1))]
    goal.wall = False
    goal.is_goal = True
    
    # create an object
    search = Search(start, grid, search_type)
    # create the agent and a food
    agent = Agent(start.center)
    food = Food(goal)
    # obstacles, water, mud and sand
    terrain_generator(grid, bricks, cols, rows)
        
# draw == while not frontier.empty()
def draw():
    delay(50)
    global rows, cols, grid, agent, k, goal, start, food, search
    w = width / cols
    h = height / rows
        
    for i in range(rows):
        for j in range(cols):
            strokeWeight(1)
            grid[i][j].display(0)        
 

    if search.is_finished is False:
        search(food.position) 
    else:
        path = search.reconstruct_path(food.position)
        k += 1
        if k < len(path):
            agent.update(path[k].center)
        else:
            k = 0
            # food counter
            food.count += 1
            print('Food Counter = ' + str(food.count))
            start = goal
            start.wall = False
            goal = grid[int(random(1, cols-1))][int(random(1, rows-1))]
            while goal.wall:
                goal = grid[int(random(1, cols-1))][int(random(1, rows-1))]
            # create an object
            search = Search(start, grid, search_type)
            # create the agent and a food
            agent = Agent(start.center)    
            # update the food position
            food.update(goal)
            redraw()
            
    agent.display(w, h)
    food.display(w, h)
