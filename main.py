from turtle import Turtle, Screen


screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")


starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions:
    new_element = Turtle("square")
    new_element.color("white")
    new_element.goto(position)
















screen.exitonclick()