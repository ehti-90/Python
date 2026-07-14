from turtle import Turtle, Screen
import pandas as pd 

screen = Screen()
tim = Turtle()
tim_write = Turtle()    #   another turtle object to write

screen.title("STATES GAME")
screen.setup(800,800)
image =".\\practice projects\\Turtle_Module_Projects\\US_States_Game\\img.gif" # turtle only supports .gif

screen.addshape(image)
tim.shape(image)
tim_write.hideturtle()

states_data  =  pd.read_csv(".\\practice projects\\Turtle_Module_Projects\\US_States_Game\\50_states.csv")
# print(state_data)

guessed_correctly = 0

game_on = True
while game_on:
    
    choice =  screen.textinput(title=f"{guessed_correctly}/50 States Correct",prompt="Guess The state") 
    choice = choice.title()
    
    
    guessed_state = states_data[states_data["state"] == choice]
    print(guessed_state.state)
    
    if choice == "Exit":
        break
    if not guessed_state.empty :
        guessed_correctly += 1
        x_cor = guessed_state.x.item()    ##.item() extracts the single value from a one-element Series.
        y_cor = guessed_state.y.item()
        tim_write.penup()
        tim_write.goto(x_cor,y_cor)
        tim_write.write(guessed_state.state.item())
    
        
        
        

screen.mainloop()