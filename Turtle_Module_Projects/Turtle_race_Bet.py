from turtle import Turtle, Screen
import random

''' 
This a small turtle race bet project that uses the turtle module in python. 
User chooses their turtle colour and Bet to Win.

'''

s = Screen()
s.setup(600,500) 

color  = ["blue","orange","red","yellow","black","green"]  # colours of different turtles object
y_pos = [0,30,60,-30,-60,-90]   # y position on the window of turtles

race_on = False
all_turtles = []

for index in range(6):  # creating 6 turtle objects
    tim = Turtle(shape="turtle")       
    tim.color(color[index])
    tim.penup()
    tim.setposition(x=-290,y=y_pos[index])
    all_turtles.append(tim)

choice = s.textinput(title="BET", prompt="Enter Turtle colour to bet :")

if choice:
    race_on = True
    
while race_on:
    
    for t in all_turtles:
        
        if t.xcor() >= 255: # take out x-coordinate of current turtle object called t
            race_on = False
            
            win_colour = t.pencolor()   # we store winning turtle pen colour
            if win_colour == choice:
                print(f"Your color {choice} Won")
            else:
                print(f"{t.pencolor()} Won - You Lost")
        
        rand_dist = random.randint(3,10)
        t.forward(rand_dist)
            
    

s.mainloop()