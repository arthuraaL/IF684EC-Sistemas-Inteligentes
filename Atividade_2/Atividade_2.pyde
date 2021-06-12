from vehicle import Vehicle
from food import Food

def setup():
    global vehicle
    global food
    size(640, 320)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, fat=False)
    food = Food()
    
def draw():
    background(0)
    fill(255)
    textSize(20)
    text('Food = ' + str(food.counter), 0, height-10)
    
    vehicle.arrive(food.position)
    if vehicle.desired.mag() < 0.5:
        food.counter += 1
        food.update(width/2, height/2)
        if vehicle.fat:
            vehicle.r += 1
    
    food.display()    
    vehicle.update()
    vehicle.display()
