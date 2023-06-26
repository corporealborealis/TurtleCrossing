import time
import turtle
from turtle import Turtle, Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title('Crossy Road')
screen.tracer(0)


player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')




game_is_on = True
game_loop = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_loop % 6 == 0:
        car.spawn_cars()

    car.move()

    game_loop += 1

    for coordinates in car.cars:
        car_coord = coordinates.position()
        if player.distance(car_coord) < 20:
            turtle.write('GAME OVER', align= 'center', font=("Courier", 24, "normal"))
            game_is_on = False

    if player.clear_stage() == True:
        car.increase_speed()
        scoreboard.update_score()


screen.exitonclick()


