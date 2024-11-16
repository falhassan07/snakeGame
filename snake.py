from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.elements = []
        self.create_snake()
        self.snake_head = self.elements[0] 

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
        self.snake_head.forward(MOVE_DISTANCE) 

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)


    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)


    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)


    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
