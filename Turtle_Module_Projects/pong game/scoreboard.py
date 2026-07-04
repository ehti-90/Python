from turtle import Turtle, Screen

class ScoreBall(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 38, "italic"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 38, "italic"))
        
        
    def update_board(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 38, "italic"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 38, "italic"))
    
    def score_update_left(self):
        self.l_score += 1
        self.update_board()

    
    def score_update_right(self):
        self.r_score += 1 
        self.update_board()
        
        