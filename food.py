from turtle import Turtle 
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.new_position()
    

    def new_position(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))

