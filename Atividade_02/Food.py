# Food class
class Food():
    
    # Randomly initializes object in a random place
    def __init__(self):
        self.position = PVector(random(0, width), random(0, height))
        self.r = 6
        self.count = 0

    # Updates the object, positioning it in a random position
    def update(self):
        self.position = PVector(random(0, width), random(0, height))

    # Shows the object in screen
    def display(self):
        fill(0, 255, 0)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
