# Food class
class Food():
    
    # Randomly initializes object in a random place
    def __init__(self, goal):
        self.position = goal
        self.r = 3
        self.count = 0

    # Updates the object, positioning it in a random position
    def update(self, new_goal):
        self.position = new_goal

    # Shows the object in screen
    def display(self, w, h):
        fill(0, 255, 0)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            rect((self.position.column * w) + w / 2, (self.position.row * h) + h / 2 , self.r, self.r)
