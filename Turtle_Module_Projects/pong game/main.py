from turtle import Turtle, Screen
from paddle import CreatePadddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")  
screen.tracer(0)    # delay turtle drawing

r_paddle = CreatePadddle((370,0))
l_paddle = CreatePadddle((-370,0))
    
screen.listen()
screen.onkeypress(fun=r_paddle.move_f,key="Up")
screen.onkeypress(fun=r_paddle.move_b,key="Down")

screen.onkeypress(fun=l_paddle.move_f,key="w")
screen.onkeypress(fun=l_paddle.move_b,key="s")

game_on = True
while game_on:
    screen.update() #update continously

screen.mainloop()