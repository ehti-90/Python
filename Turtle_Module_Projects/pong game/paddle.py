from turtle import Turtle, Screen

class CreatePadddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.penup()
        self.setposition(position)
        self.setheading(90)       
        
     
        
    def move_f(self):
        self.fd(10)
    
    def move_b(self):
        self.backward(10)