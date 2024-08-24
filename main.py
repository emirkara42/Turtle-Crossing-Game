import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = []
for _ in range(10):
    car_manager = CarManager()
    cars.append(car_manager)
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()

    for car in cars:
        car.move()
        if car.xcor() < -320:
            car.generate()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 250:
        player.restart()
        scoreboard.score_point()



screen.exitonclick()




