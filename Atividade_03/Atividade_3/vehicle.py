# Vehicle class
class Vehicle():
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -1)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.2

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset acceleration to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(255,0,0)
        stroke(200)
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
