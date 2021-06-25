class Graph:
    def __init__(self, column, row, w, h, f):
        self.column = column
        self.row = row
        # width
        self.w = w
        # height
        self.h = h
        # cost
        self.f = f
        self.neighbors = []
        #self.center = (x + self.w / 2, y + self.h / 2)
    
    def __call__(self):
        pass
    
    def add_neighbors(self, nodes):
        columns = 10 # por enquanto
        rows = 10
        if self.row > 0:
            self.neighbors.append(nodes[self.row - 1][self.column])
        if self.column > 0:
            self.neighbors.append(nodes[self.row][self.column - 1])
        if self.column < columns - 1:
            self.neighbors.append(nodes[self.row][self.column + 1])
        if self.row < rows - 1:
            self.neighbors.append(nodes[self.row + 1][self.column])
            
            
        
            
    def display(self, c, is_neighbor=False):
        stroke(c)
        fill(255)
        rect(self.column * self.w, self.row * self.h, self.w, self.h)
