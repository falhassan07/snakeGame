from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.elements = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_element = Turtle("square")
            new_element.color("white")
            new_element.penup()
            new_element.goto(position) 
            self.elements.append(new_element)

    
    def move(self):
        for elem_num in range(len(self.elements)-1, 0, -1):
            new_x = self.elements[elem_num-1].xcor()
            new_y = self.elements[elem_num-1].ycor()
            self.elements[elem_num].goto(new_x, new_y)
        self.elements[0].forward(MOVE_DISTANCE) 