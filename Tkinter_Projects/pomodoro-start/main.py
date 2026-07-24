
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.minsize(width=600, height=400)
window.config(padx=50,pady=50,background=PINK)

# Timer Label
timer_text = tk.Label(window,text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=PINK)
timer_text.grid(row=0,column=2)
#TICK LABEL
tick_label = tk.Label(window,text="✔",font=(FONT_NAME),bg=PINK,fg="green")
tick_label.grid(row=2,column=2)


#START BUTTON
start_button = tk.Button(window,text="START",font=(FONT_NAME,12,"bold"),fg="blue",bg="white",padx=10,pady=6)
start_button.grid(row=2,column=0)
#RESET BUTTON
reset_button = tk.Button(window,text="RESET",font=(FONT_NAME,12,"bold"),fg="blue",bg="white",padx=10,pady=6)
reset_button.grid(row=2,column=3)


canvas = tk.Canvas(width=300,height=300,bg=PINK,highlightthickness=0) 
tomato_image = tk.PhotoImage(file="tomato.png") # reads photo from a file at a particular location
canvas.create_image(150,150,image=tomato_image)# coordinates on the canvas
canvas.create_text(150,150,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))# writing on top of canvas image
canvas.grid(row=1,column=2)


window.mainloop()