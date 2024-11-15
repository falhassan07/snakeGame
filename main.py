from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)


starting_positions = [(0,0),(-20,0),(-40,0)]
elements = []
for position in starting_positions:
    new_element = Turtle("square")
    new_element.color("white")
    new_element.penup()
    new_element.goto(position) 
    elements.append(new_element)

game_is_on = True
 

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for element in elements:
        element.forward(20) 
        















screen.exitonclick()