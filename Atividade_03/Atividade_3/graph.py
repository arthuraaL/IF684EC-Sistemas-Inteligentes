class Graph:
    '''
    Creates a graph

    Parameters
    ----------
    column : int
        Column of the cell
    row: int
        Row of the cell
    w: int
        Width of the cell
    h: int
        Height of the cell
    f: float
        Cost of the cell
        
    Attributes
    ----------
    neighbors: list
        This is where we store the neighbors of the node
    '''
    def __init__(self, column, row, w, h, f):
        self.column = column
        self.row = row
        self.w = w
        # height
        self.h = h
        self.f = f
        self.neighbors = []
        self.center = PVector(self.column, self.row)
        self.wall = False 
        self.water = False
        self.sand = False
        self.path = []
        
    
    def add_neighbors(self, nodes):
        '''Add the neighbors of the nodes
        
        Parameters
        ----------
        nodes: Graph
            The nodes are used to access the neighbors of each cell
        '''
        columns = 20 #temporario
        rows = 20
        if self.row > 0:
            self.neighbors.append(nodes[self.row - 1][self.column])
        if self.column > 0:
            self.neighbors.append(nodes[self.row][self.column - 1])
        if self.column < columns - 1:
            self.neighbors.append(nodes[self.row][self.column + 1])
        if self.row < rows - 1:
            self.neighbors.append(nodes[self.row + 1][self.column])
    
    def display(self, c=0, is_goal=False, terrain='sand'):
        '''Display grid to debug
        
        Parameters
        ----------
        c: color
        is_goal: bool:
            If is in the goal, it should color the path
        '''        
        stroke(c)
        fill(color(194, 178, 128))
        if self.sand:
            fill(color(112, 84, 62))
        if self.water:
            fill(color(57, 163, 192))
        if self.wall:
            fill(0)
        if is_goal:
            fill(c)
        rect(self.column * self.w, self.row * self.h, self.w, self.h)
