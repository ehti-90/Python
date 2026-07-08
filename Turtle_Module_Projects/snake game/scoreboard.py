from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 #   for higest score
        
        self.color("white") # we are making the colour of turtle that make sthe scoreboard white
        self.hideturtle()   # we hide it
        self.penup()
        self.goto(0, 370)
        self.pendown()
        self.write_score()
    
    def write_score(self):
        self.write(f"Score = {self.score} : High Score = {self.high_score}", False, "center", ('Arial', 20, 'normal'))
      
    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
        
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()
        
    # def game_over(self):
    #     self.goto(0,0,)
    #     self.write("GAME OVER", False, "center", ('Arial', 20, 'normal'))
        