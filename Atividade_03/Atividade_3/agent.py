from graph import Graph
class Agent:
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -1)
        self.position = PVector(x, y)
        self.r = 10
        self.maxspeed = 4
        self.maxforce = 0.2
        
    # Method to update location
    def update(self, x, y):
        # # Update velocity
        # self.velocity.add(self.acceleration)
        # # Limit speed
        # self.velocity.limit(self.maxspeed)
        # self.position.add(self.velocity)
        # # Reset acceleration to 0 each cycle
        # self.acceleration.mult(0)
        self.position = PVector(x, y)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, target):
        # A vector pointing from the location to the target
        self.desired = target - self.position
        d = self.desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            self.desired.setMag(m)
        else:
            self.desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = self.desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
    
    def display(self, w, h):
        fill(255,0,0)
        stroke(200)
        strokeWeight(1)
        with pushMatrix():
            circle((self.position.x * w) + w / 2, (self.position.y * h) + h / 2, self.r)
