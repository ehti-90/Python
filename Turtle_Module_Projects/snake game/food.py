from turtle import Turtle
import random

class Food(Turtle): # we inherit from Turtle class
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5) # make the turtle smaller circle
        self.speed("fastest")
        self.new_location()
        
    def new_location(self):
        rand_x = random.randint(-390,390)
        rand_y = random.randint(-390,390)
        self.goto(rand_x,rand_y)
        