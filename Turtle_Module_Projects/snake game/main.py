from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import random
import time



screen = Screen()

screen.bgcolor("black")
screen.setup(800,800)
screen.tracer(0)            # off the automatic screen update: if instead of 0 theer was 10 it would have been--
screen.title("Snake Game")  # updated after 10 turtle movement

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

    
game_on = True

while game_on:
    
    screen.update() #   after the ops in loop is made update now
    time.sleep(0.1) # add o.2 sec delay after screen update
    
    snake.move()
    
    if snake.head.distance(food) < 15:  # this .distance check distance between snake ob and food object
        food.new_location()             # when they get this close the  food must goto another rand place
        snake.extend()
        score.update_score() 
        
    # checks if snake crossed window borders   
    if snake.head.xcor() > 390 or  snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < - 390:
        score.reset()
        snake.reset_snake()
        
    # check if snake head touches any segment
    for seg in snake.all_turtles[1:]:
        
        if snake.head.distance(seg) < 10:   # if distance between any seg and head is less then 10 then game over 
            score.reset()
            snake.reset_snake()

            

screen.mainloop()