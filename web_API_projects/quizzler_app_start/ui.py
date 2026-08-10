THEME_COLOR = "#375362"
from tkinter import *
from pathlib import Path
from quiz_brain import QuizBrain



BASE_DIR = Path(__file__).resolve().parent
t_button_path = BASE_DIR / "images" / "true.png"
f_button_path = BASE_DIR / "images" / "false.png"


class QuizzInterface:
    
    def __init__(self,quizz_brain: QuizBrain): #of type quizz brain this object we working with
        self.quizz = quizz_brain #quizz brain object
        self.window = Tk()
        self.window.title("Quizzler Game")
        self.window.minsize(width=600,height=700)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        
        #label
        self.score_label = Label(text=f"Score = {self.quizz.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=2,columnspan=1)
        #images
        self.true_button_image  = PhotoImage(file=t_button_path)
        self.false_button_image  = PhotoImage(file=f_button_path)
        
        #canvas 
        self.canvas = Canvas(width=550,height=450,bg=THEME_COLOR,highlightthickness=0)
        self.question_text = self.canvas.create_text(300,210,width=540,text="Testing",fill="white",font=("abadi",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=3,pady=40)
        
        
        #buttons
        self.tick_button = Button(image=self.true_button_image,highlightthickness=0,command=self.true_pressed)
        self.tick_button.grid(row=2, column=0,columnspan=2)
        
        self.false_button = Button(image=self.false_button_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1,columnspan=2)
        
        self.next_question()
        
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg=THEME_COLOR)
        
        if self.quizz.still_has_questions():
            q_text = self.quizz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.tick_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"End of Questions\nTotal Score = {self.quizz.score}/ {len(self.quizz.question_list)} ")

    def true_pressed(self):
        is_what = self.quizz.check_answer("True")
        self.feedback(is_what)
        
        
    def false_pressed(self):
        is_what = self.quizz.check_answer("False")
        self.feedback(is_what)
        
    def feedback(self,is_what):
        if is_what :
            self.score_label.config(text=f"Score : {self.quizz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000,func=self.next_question)

