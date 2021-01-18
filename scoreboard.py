from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.LVL = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-292, 260)
        self.write(f"Level {self.LVL}", font=FONT)
    def scoreup(self):
        self.LVL += 1
        self.clear()
        self.write(f"Level {self.LVL}", font=FONT)
    def new(self):
        self.clear()
        self.goto(-150,260)
        self.color("red")
        self.write(f"You LOSE!", font=("Arial", 24, "normal"))
    def new1(self):
        self.clear()
        self.goto(-150,260)
        self.color("green")
        self.write(f"You WIN!", font=("Arial", 24, "normal"))



