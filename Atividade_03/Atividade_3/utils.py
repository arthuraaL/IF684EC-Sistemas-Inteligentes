from collections import deque

class BFS:
    def __init__(self, start, graph):
        self._start = start
        self._graph = graph
        self.frontier = deque()
        self.frontier.append(self._start)
        self.came_from = dict()
        self.came_from[self._start] = None
        
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
                path = []
                temp = current
                path.append(temp)
                while (self.came_from[temp] != None):
                    path.append(self.came_from[temp])
                    temp = self.came_from[temp]
                current.path = path
                for i in path:
                    i.display(color(120,4,200), is_goal=True)      
                noLoop()
            for neighbor in current.neighbors:
                if neighbor not in self.came_from:
                    self.frontier.append(neighbor)
                    self.came_from[neighbor] = current

def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]
    
    
