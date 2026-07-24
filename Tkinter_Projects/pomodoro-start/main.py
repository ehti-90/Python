
import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
t = None # global for to stop .after()
# ---------------------------- CHANGE BACKGROUNG MODE  ------------------------------- # 
def turn_dark():
    tick_label.config(bg="black")
    timer_text.config(bg="black")
    canvas.config(bg="black")
    window.config(background="black")

def turn_pink():
    tick_label.config(bg=PINK)
    timer_text.config(bg=PINK)
    canvas.config(bg=PINK)
    window.config(background=PINK)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(t) # stop time
    
    canvas.itemconfig(count_time, text="00:00")
    timer_text.config(text="Timer")
    tick_label.config(text="")
    global reps 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    # long break after 4 round of 25m work and 4 rounds of 5m break
    if reps % 8 == 0:
        timer_text.config(text="Long Break",fg=RED) # change timer_label text through config because its not on canvas
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_text.config(text="Short Break",fg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer_text.config(text="Work Time",fg=GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global t
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
   
    
        
    canvas.itemconfig(count_time, text=f"{count_min}:{count_sec}") # canvas changes through .itemconfig instead of .coonfig : windows
    if count > 0:
        t = window.after(1000,count_down,count-1) #wait for 1sec call this countdown and pass in 1 les than original
    elif count == 0: # when work time finishes break time starts 
        start_timer() # start when first round 25m finishes so we dont press button to countinue
        marks = ""
        
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.minsize(width=600, height=400)
window.config(padx=50,pady=50,background=PINK)


# Canvas 
canvas = tk.Canvas(width=300,height=300,bg=PINK,highlightthickness=0) 
tomato_image = tk.PhotoImage(file="practice projects\Tkinter_Projects\pomodoro-start\\tomato.png") # reads photo from a file at a particular location
canvas.create_image(150,150,image=tomato_image)# coordinates on the canvas
count_time = canvas.create_text(150,150,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))# writing on top of canvas image
canvas.grid(row=1,column=2)


#  Timer Label
timer_text = tk.Label(window,text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=PINK)
timer_text.grid(row=0,column=2)
#TICK LABEL
tick_label = tk.Label(window,font=(FONT_NAME),bg=PINK,fg="green")
tick_label.grid(row=2,column=2)


#START BUTTON
start_button = tk.Button(window,text="START",font=(FONT_NAME,12,"bold"),fg="blue",bg="white",padx=10,pady=6,command=start_timer)
start_button.grid(row=2,column=1)
#RESET BUTTON
reset_button = tk.Button(window,text="RESET",font=(FONT_NAME,12,"bold"),fg="blue",bg="white",padx=10,pady=6, command=reset_timer)
reset_button.grid(row=2,column=3)
# Dark Mode Button
dark_mode_button = tk.Button(window,text="Black",font=(FONT_NAME,10,"bold"),fg="white",bg="Black",padx=6,pady=6, command=turn_dark)
dark_mode_button.grid(row=0,column=0)
#Normal Mode Button
dark_mode_button = tk.Button(window,text="Pink",font=(FONT_NAME,10,"bold"),fg="white",bg=PINK,padx=15,pady=6, command=turn_pink)
dark_mode_button.grid(row=0,column=3)


window.mainloop()