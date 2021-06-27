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
                # path = []
                # temp = current
                # path.append(temp)
                # while (self.came_from[temp] != None):
                #     path.append(self.came_from[temp])
                #     temp = self.came_from[temp]
                # current.path = path
                # for i in path:
                #     i.display(color(120,4,200), is_goal=True)      
                    
            for neighbor in current.neighbors:
                if neighbor not in self.came_from:
                    self.frontier.append(neighbor)
                    self.came_from[neighbor] = current
            
            return self.came_from
                    
    # def __call__(self, goal):
    #     for i in self.came_from:
    #         strokeWeight(1)
    #         i.display(0)
    
    #     for i in self.frontier:
    #         strokeWeight(2)
    #         i.display(color(0,0,150))
            
    #     while len(self.frontier) > 0:
    #         current = self.frontier.popleft()
            
    #         if current == goal:
    #             break
            
    #         for neighbor in current.neighbors:
    #             if neighbor not in self.came_from:
    #                 self.frontier.append(neighbor)
    #                 self.came_from[neighbor] = current
        
    #     return self.came_from
    
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
    
    
