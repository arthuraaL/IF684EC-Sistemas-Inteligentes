from vehicle import Vehicle
from food import Food

def setup():
    global vehicle
    global food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2)
    food = Food()

def draw():
    background(255)
    fill(0, 100, 150)
    text('Food Counter: ' + str(food.count), 10, height-340)
    textSize(16)
    
    vehicle.update()
    vehicle.display()
    food.display()
    vehicle.arrive(food.position)
    if vehicle.desired.mag() < 0.5:
        food.count += 1
        food.update()
    

    
