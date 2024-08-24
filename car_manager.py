from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        x = random.randint(-280, 400)
        y = random.randint(-160, 160)
        self.goto(x, y)

    def generate(self):
        new_x = random.randint(300, 400)
        new_y = random.randint(-160, 160)
        self.goto(new_x, new_y)

    def move(self):
        self.forward(MOVE_DISTANCE)





