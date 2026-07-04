from turtle import Turtle, Screen

class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.setposition(0,0)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x,new_y)
        
    def upper_wall_collision(self):
        
        if self.ycor() >= 290 :
            self.y_cor *= -1
        
        elif self.ycor() <= -290:
            self.y_cor *= -1
            
    def paddle_collision(self):
        self.x_cor *= -1
        
    def reset_position(self):
        self.setpos(0,0)
        self.move_speed = 0.1
        self.x_cor *= -1
        self.y_cor *= -1
        
        
            
        
            
        