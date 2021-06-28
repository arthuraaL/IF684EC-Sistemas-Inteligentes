def heuristic(origin, ending):
    return abs(origin.row - ending.row) + abs(origin.column - ending.column)

def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]

def make_horizontal_walls(grid):
    i_wall = int(random(18))
    j_wall = int(random(18))
    h_wall = [grid[j_wall][i_wall], grid[j_wall+1][i_wall], grid[j_wall+2][i_wall]]
    for i in h_wall:
        if i.is_start or i.is_goal:
             make_horizontal_walls(grid)
        else:
            i.wall = True
    
def make_vertical_walls(grid):
    i_wall = int(random(18))
    j_wall = int(random(18))
    v_wall = [grid[j_wall][i_wall], grid[j_wall][i_wall+1], grid[j_wall][i_wall+2]]
    
    for i in v_wall:
        if i.is_start or i.is_goal:
             make_vertical_walls(grid)
        else:
            i.wall = True

def make_sand(grid):
    orientation = int(random(2))
    spread_point_x = int(random(13))
    spread_point_y = int(random(13))
    if orientation == 0: #Horizontal Sand Rectangle
        for i in range(7):
            for j in range(4):
                if not grid[spread_point_x + i][spread_point_y + j].wall:
                    grid[spread_point_x + i][spread_point_y + j].sand = True
                    grid[spread_point_x + i][spread_point_y + j].f = 5
                    grid[spread_point_x + i][spread_point_y + j]
    else: #Vertical Sand Rectangle
        for i in range(4):
            for j in range(7):
                if not grid[spread_point_x + i][spread_point_y + j].wall:
                    grid[spread_point_x + i][spread_point_y + j].sand = True
                    grid[spread_point_x + i][spread_point_y + j].f = 5
                    grid[spread_point_x + i][spread_point_y + j]

def make_water(grid):
    spread_point_x = int(random(15))
    spread_point_y = int(random(15))
    for i in range(5):
        for j in range(5):
            if not grid[spread_point_x + i][spread_point_y + j].wall and not grid[spread_point_x + i][spread_point_y + j].sand:
                grid[spread_point_x + i][spread_point_y + j].water = True
                grid[spread_point_x + i][spread_point_y + j].f = 10 
                grid[spread_point_x + i][spread_point_y + j]
                
def terrain_generator(grid):
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    
    make_vertical_walls(grid)
    make_horizontal_walls(grid)
    
    make_sand(grid)
    make_water(grid)
