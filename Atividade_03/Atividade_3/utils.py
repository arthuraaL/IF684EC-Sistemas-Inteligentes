from collections import deque

class BFS:
    def __init__(self, start, graph):
        self._start = start
        self._graph = graph
        self.frontier = deque()
        self.frontier.append(self._start)
        self.came_from = dict()
        self.came_from[self._start] = None
        self.is_finish = False
        
    def __call__(self, goal):
        for i in self.came_from:
            strokeWeight(1)
            i.display(0)
    
        for i in self.frontier:
            strokeWeight(2)
            i.display(color(0,0,150))
            
        if len(self.frontier) > 0:
            current = self.frontier.popleft()
            
            if current == goal:
                self.is_finish = True   
                    
            for neighbor in current.neighbors:
                if neighbor not in self.came_from and not neighbor.wall:
                    self.frontier.append(neighbor)
                    self.came_from[neighbor] = current
            
            return self.came_from
    
    def reconstruct_path(self, came_from, goal):
        current = goal
        path = []
        while current != self._start:
            path.append(self.came_from[current])
            current = self.came_from[current]
        path.append(self._start)
        path.reverse()
        
        for i in path:
            i.display(color(120,4,200), is_goal=True)
        
        return path

def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]

def make_horizontal_walls(grid):
    i_wall = int(random(10))
    j_wall = int(random(10))
    h_wall = [grid[j_wall][i_wall], grid[j_wall+1][i_wall], grid[j_wall+2][i_wall]]
    for i in h_wall:
        i.wall = True
    
def make_vertical_walls(grid):
    i_wall = int(random(10))
    j_wall = int(random(10))
    h_wall = [grid[j_wall][i_wall], grid[j_wall][i_wall+1], grid[j_wall][i_wall+2]]
    for i in h_wall:
        i.wall = True    
    
