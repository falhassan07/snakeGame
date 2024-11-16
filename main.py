from turtle import Screen
from snake import *
from food import Food 
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
 

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #check collision with food 
    if snake.snake_head.distance(food) < 15:
        food.new_position()
        scoreboard.increase_score()














screen.exitonclick()