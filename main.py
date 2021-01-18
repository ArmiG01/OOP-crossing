import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car = CarManager()
screen.listen()
screen.onkeypress(player.go, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.createcar()
    car.carsgo()
    for cay in car.cars:
        if score.LVL <= 3:
            if player.distance(cay) < 20:
                score.new()
                game_is_on = False
            elif player.ycor() == 280:
                car.speed += 5
                score.scoreup()
                player.ret()
        else:
            game_is_on = False
            score.new1()

    screen.update()
screen.exitonclick()