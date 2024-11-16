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
    time.sleep(0.06)
    snake.move()


    #check collision with food 
    if snake.snake_head.distance(food) < 15:
        food.new_position()
        snake.extend()
        scoreboard.increase_score()


    #detect collision with wall 
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detec collision with tail 
    for element in snake.elements[1:]:
        if snake.snake_head.distance(element) < 10:
            game_is_on = False
            scoreboard.game_over()
            











screen.exitonclick()