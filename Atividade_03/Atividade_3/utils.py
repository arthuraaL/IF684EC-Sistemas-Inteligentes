def BFS(frontier, came_from, goal):
    if len(frontier) > 0:
        current = frontier.popleft()
        if current == goal:
            path = []
            temp = current
            path.append(temp)
            while (came_from[temp] != None):
                path.append(came_from[temp])
                temp = came_from[temp]
            noLoop()
            for i in path:
                i.display(color(120,4,200), is_goal=True)
        for neighbor in current.neighbors:
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current
                
                
def make_grid(rows, cols):
    ''' Returns a empty grid '''
    return [[0 for col in range(cols)] for row in range(rows)]
    
    
