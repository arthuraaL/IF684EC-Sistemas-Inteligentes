def heuristic(origin, ending):
    return abs(origin.row - ending.row) + abs(origin.column - ending.column)

def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]

def make_horizontal_walls(grid, bricks, cols, rows):
    i_wall = int(random(rows - bricks))
    j_wall = int(random(cols - bricks))
    generate = True
    while generate:
        generate = False
        for i in range(bricks):
            if grid[j_wall+i][i_wall].is_start == True or grid[j_wall+i][i_wall].is_goal == True:
                i_wall = int(random(rows - bricks))
                j_wall = int(random(cols - bricks))
                generate = True
    
    for i in range(bricks):
        grid[j_wall+i][i_wall].wall = True
                
    
def make_vertical_walls(grid, bricks, cols, rows):
    i_wall = int(random(rows - bricks))
    j_wall = int(random(cols - bricks))    
    generate = True
    while generate:
        generate = False
        for i in range(bricks):
            if grid[j_wall][i_wall+i].is_start == True or grid[j_wall][i_wall+i].is_goal == True:
                i_wall = int(random(rows - bricks))
                j_wall = int(random(cols - bricks))
                generate = True
    
    for i in range(bricks):
        grid[j_wall][i_wall+i].wall = True

def make_sand(grid):
    orientation = int(random(2))
    spread_point_x = int(random(17))
    spread_point_y = int(random(17))
    generate = True
    if orientation == 0: #Horizontal Sand Rectangle
        while generate:
            generate = False
            for i in range(3):
                for j in range(2):
                    if grid[spread_point_x + i][spread_point_y + j].wall == True:
                        spread_point_x = int(random(17))
                        spread_point_y = int(random(17))
                        generate = True
        for i in range(3):
            for j in range(2):
                if not grid[spread_point_x + i][spread_point_y + j].wall:
                    grid[spread_point_x + i][spread_point_y + j].sand = True
                    grid[spread_point_x + i][spread_point_y + j].f = 1
                    grid[spread_point_x + i][spread_point_y + j]
                    
    else: #Vertical Sand Rectangle
        while generate:
            generate = False
            for i in range(2):
                for j in range(3):
                    if grid[spread_point_x + i][spread_point_y + j].wall == True:
                        spread_point_x = int(random(17))
                        spread_point_y = int(random(17))
                        generate = True
        for i in range(2):
            for j in range(3):
                if not grid[spread_point_x + i][spread_point_y + j].wall:
                    grid[spread_point_x + i][spread_point_y + j].sand = True
                    grid[spread_point_x + i][spread_point_y + j].f = 1
                    grid[spread_point_x + i][spread_point_y + j]

def make_mud(grid):
    orientation = int(random(2))
    spread_point_x = int(random(13))
    spread_point_y = int(random(13))
    generate = True
    if orientation == 0: #Horizontal Mud Rectangle
        while generate:
            generate = False
            for i in range(7):
                for j in range(4):
                    if grid[spread_point_x + i][spread_point_y + j].wall == True or grid[spread_point_x + i][spread_point_y + j].sand == True:
                        spread_point_x = int(random(13))
                        spread_point_y = int(random(13))
                        generate = True
        for i in range(7):
            for j in range(4):
                if not grid[spread_point_x + i][spread_point_y + j].wall and not grid[spread_point_x + i][spread_point_y + j].sand:
                    grid[spread_point_x + i][spread_point_y + j].mud = True
                    grid[spread_point_x + i][spread_point_y + j].f = 5
                    grid[spread_point_x + i][spread_point_y + j]
                    
    else: #Vertical Mud Rectangle
        while generate:
            generate = False
            for i in range(4):
                for j in range(7):
                    if grid[spread_point_x + i][spread_point_y + j].wall == True or grid[spread_point_x + i][spread_point_y + j].sand == True:
                        spread_point_x = int(random(13))
                        spread_point_y = int(random(13))
                        generate = True
        for i in range(4):
            for j in range(7):
                if not grid[spread_point_x + i][spread_point_y + j].wall:
                    grid[spread_point_x + i][spread_point_y + j].mud = True
                    grid[spread_point_x + i][spread_point_y + j].f = 5
                    grid[spread_point_x + i][spread_point_y + j]
                    
def make_water(grid):
    spread_point_x = int(random(15))
    spread_point_y = int(random(15))
    generate = True
    while generate:
        generate = False
        for i in range(5):
            for j in range(5):
                if grid[spread_point_x + i][spread_point_y + j].wall == True or grid[spread_point_x + i][spread_point_y + j].sand == True or grid[spread_point_x + i][spread_point_y + j].mud == True:
                    spread_point_x = int(random(15))
                    spread_point_y = int(random(15))
                    generate = True
    for i in range(5):
        for j in range(5):
            if not grid[spread_point_x + i][spread_point_y + j].wall and not grid[spread_point_x + i][spread_point_y + j].sand and not grid[spread_point_x + i][spread_point_y + j].mud:
                grid[spread_point_x + i][spread_point_y + j].water = True
                grid[spread_point_x + i][spread_point_y + j].f = 10 
                grid[spread_point_x + i][spread_point_y + j]
                
def terrain_generator(grid, bricks, cols, rows):
    make_vertical_walls(grid, bricks, cols, rows)
    make_horizontal_walls(grid, bricks, cols, rows)
    
    make_vertical_walls(grid, bricks, cols, rows)
    make_horizontal_walls(grid, bricks, cols, rows)
    
    make_vertical_walls(grid, bricks, cols, rows)
    make_horizontal_walls(grid, bricks, rows, rows)
    
    make_sand(grid)
    make_sand(grid)
    make_mud(grid)
    make_water(grid)
