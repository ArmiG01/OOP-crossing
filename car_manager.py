from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = 5
        self.hideturtle()
    def createcar(self):
        if randint(1,5) == 2:
            new = Turtle("square")
            new.shapesize(1, 2)
            new.color(choice(COLORS))
            new.penup()
            new.goto(320, randint(-250, 260))
            self.cars.append(new)
    def carsgo(self):
        for car in self.cars:
            car.backward(self.speed)