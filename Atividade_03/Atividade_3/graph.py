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
        Cost of the path -> f(n) = g(n) + h(n)
        
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
        self.path = []
    
    def add_neighbors(self, nodes):
        '''Add the neighbors of the nodes
        
        Parameters
        ----------
        nodes: Graph
            The nodes is used to access the neighbors of each cell
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
    
    def display(self, c, is_goal=False):
        '''Display grid to debug
        
        Parameters
        ----------
        c: color
        is_goal: bool:
            If is in the goal, it should color the path
        '''        
        stroke(c)
        fill(255)
        if is_goal:
            fill(c)
        rect(self.column * self.w, self.row * self.h, self.w, self.h)
