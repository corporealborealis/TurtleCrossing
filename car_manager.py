from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 # Increase speed as user levels up


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.initial_distance = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        car = Turtle(shape='square')
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        starting_x = 280
        starting_y = random.randint(-230,230)
        car.goto(starting_x,starting_y)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.initial_distance += MOVE_INCREMENT

