# The "Food" class

class Food():

    def __init__(self):
        self.position = PVector(0, 0)
        self.counter = 0
        self.r = 6

    # Method to update location
    def update(self, x, y):
        self.position = PVector(random(0, x), random(0, y))

    def display(self):
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
