from collections import deque
from queue import PriorityQueue as pqueue
from utils import heuristic, make_grid, make_horizontal_walls, make_vertical_walls, make_sand, make_water


class Search:
    def __init__(self, start, graph, algorithm):
        self._start = start
        self._graph = graph
        
        self.is_finished = False
        self.algorithm = algorithm
        
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[self._start] = None
        self.cost_so_far[self._start] = 0
        
        if self.algorithm == 'bfs' or self.algorithm == 'dfs':
            self.frontier = deque()
            self.frontier.append(self._start)       
        elif self.algorithm == 'ucs' or self.algorithm == 'greedy' or self.algorithm == 'a_star':
            self.frontier = pqueue()
            self.frontier.insert((self._start.f, self._start))

            
    def __call__(self, goal):
        if self.algorithm == 'bfs':
            for i in self.came_from:
                strokeWeight(2)
                i.display(color(150,0,0))
        
            for i in self.frontier:
                strokeWeight(2)
                i.display(color(0,0,150))
                
            if len(self.frontier) > 0:
                current = self.frontier.popleft()
                
                if current == goal:
                    self.is_finished = True   
                        
                for neighbor in current.neighbors:
                    if neighbor not in self.came_from and not neighbor.wall:
                        self.frontier.append(neighbor)
                        self.came_from[neighbor] = current
                
                return self.came_from
            
        elif self.algorithm == 'dfs':
            for i in self.came_from:
                strokeWeight(2)
                i.display(color(150,0,0))
        
            for i in self.frontier:
                strokeWeight(2)
                i.display(color(0,0,150))
                
            if len(self.frontier) > 0:
                current = self.frontier.pop()
                
                if current == goal:
                    self.is_finished = True   
                        
                for neighbor in current.neighbors:
                    if neighbor not in self.came_from and not neighbor.wall:
                        self.frontier.append(neighbor)
                        self.came_from[neighbor] = current
                
                return self.came_from  
            
        elif self.algorithm == 'ucs':
            for i in self.came_from:
                strokeWeight(2)
                i.display(color(150,0,0))
        
            for i in self.frontier.queue:
                strokeWeight(2)
                i[1].display(color(0,0,150))
            
            if len(self.frontier.queue) > 0:
                current = self.frontier.delete()
                
                if current == goal:
                    self.is_finished = True
                    
                for neighbor in current.neighbors:
                    new_cost = self.cost_so_far[current] + neighbor.f
                    if (neighbor not in self.came_from or new_cost < self.cost_so_far[neighbor]) and not neighbor.wall:
                        self.cost_so_far[neighbor] = new_cost
                        priority = new_cost
                        self.frontier.insert((priority, neighbor))
                        self.came_from[neighbor] = current
                
                return self.came_from            
     
        elif self.algorithm == 'greedy':
            for i in self.came_from:
                strokeWeight(2)
                i.display(color(150,0,0))
        
            for i in self.frontier.queue:
                strokeWeight(2)
                i[1].display(color(0,0,150))
            
            if len(self.frontier.queue) > 0:
                current = self.frontier.delete()
                if current == goal:
                    self.is_finished = True
                    
                for neighbor in current.neighbors:
                    if neighbor not in self.came_from and not neighbor.wall:
                        priority = heuristic(neighbor, goal)
                        self.frontier.insert((priority, neighbor))
                        self.came_from[neighbor] = current
            
                return self.came_from            
            
        elif self.algorithm == 'a_star':
            for i in self.came_from:
                strokeWeight(2)
                i.display(color(150,0,0))
        
            for i in self.frontier.queue:
                strokeWeight(2)
                i[1].display(color(0,0,150))
            
            if len(self.frontier.queue) > 0:
                current = self.frontier.delete()
                
                if current == goal:
                    self.is_finished = True
                    
                for neighbor in current.neighbors:
                    new_cost = self.cost_so_far[current] + neighbor.f
                    if (neighbor not in self.came_from or new_cost < self.cost_so_far[neighbor]) and not neighbor.wall:
                        self.cost_so_far[neighbor] = new_cost
                        priority = new_cost + heuristic(neighbor, goal)
                        self.frontier.insert((priority, neighbor))
                        self.came_from[neighbor] = current
            
                return self.came_from            
            
        
    def reconstruct_path(self, goal):
        current = goal
        path = []
        path.append(goal)
        while current != self._start:
            path.append(self.came_from[current])
            current = self.came_from[current]
        path.append(self._start)
        path.reverse()
        
        for i in path:
            i.display(color(120,4,200), is_goal=True)
        
        return path
