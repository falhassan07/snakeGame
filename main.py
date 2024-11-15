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
    for elem_num in range(len(elements)-1, 0, -1):
        new_x = elements[elem_num-1].xcor()
        new_y = elements[elem_num-1].ycor()
        elements[elem_num].goto(new_x, new_y)
    elements[0].forward(20)
    elements[0].left(90)
        















screen.exitonclick()