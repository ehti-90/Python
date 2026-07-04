from turtle import Turtle, Screen
from paddle import CreatePadddle
from ball import CreateBall
from scoreboard import ScoreBall
import time

def quit():
    global game_on
    
    choice = screen.textinput(title="Continue/Finish", prompt="Do You want To Continue or Finish (c/f):")
    if choice == "f":
        screen.bye()
    else:
        print("Continued")
        screen.listen()
        
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")  
screen.tracer(0)    # delay turtle drawing


r_paddle = CreatePadddle((370,0))
l_paddle = CreatePadddle((-370,0))

ball =   CreateBall() 
score = ScoreBall()

screen.listen()
screen.onkeypress(fun=r_paddle.move_f,key="Up")
screen.onkeypress(fun=r_paddle.move_b,key="Down")

screen.onkeypress(fun=l_paddle.move_f,key="w")
screen.onkeypress(fun=l_paddle.move_b,key="s")
screen.onkeypress(fun=quit, key="q")    #press q to quite the game 

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update() #update continously
    
    ball.move() 
    # uppper window contact 
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.upper_wall_collision()
    
    # contact with paddle
    if ball.distance(r_paddle) <50 and ball.xcor() > 340:
        ball.paddle_collision()
        ball.move_speed *= 0.9


    elif ball.distance(l_paddle) <50 and ball.xcor() < -340:
        ball.paddle_collision()
        ball.move_speed *= 0.9

        
    # check if any player misses and out of window then update score
    if ball.xcor() > 390 :
        ball.reset_position()
        score.score_update_left()
        
    
    if ball.xcor() < -390:
        ball.reset_position()
        score.score_update_right()
    
        
screen.mainloop()