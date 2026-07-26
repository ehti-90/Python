# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=700,height=500)
window.config(padx=50,pady=40)



#Canvas 
canvas = tk.Canvas(bg="pink",width=250,height=200)
lock_image = tk.PhotoImage(file="practice projects\Tkinter_Projects\password-manager\logo.png")
canvas.create_image(150,100,image=lock_image) # x and y on canvas
canvas.grid(row=0,column=1)


#WEBSITE LABEL
web_label = tk.Label(window,text="Website : ",font=("calibri",12),fg="black",bg="pink")
web_label.grid(row=1,column=0)
#EMAIL LABEL
email_label = tk.Label(window,text="Email/User_name : ",font=("calibri",12),fg="black",bg="yellow")
email_label.grid(row=2,column=0)
#PASSWORD LABEL
pass_label = tk.Label(window,text="Password : ",font=("calibri",12),fg="black",bg="pink")
pass_label.grid(row=3,column=0)


#ADD BUTTON
add_butt = tk.Button(window,text="ADD",font=("calibri",12),padx=150,pady=0)
add_butt.grid(row=4,column=1,columnspan=2)
#GENERATE BUTTON
generate_pass = tk.Button(window,text="Generate Password",font=("calibri",12),bg="orange",)
generate_pass.grid(row=3,column=2,columnspan=2)


# WEB INPUT
web_input = tk.Entry(width=50)
web_input.grid(row=1,column=1,columnspan=2)
#EMAIL INPUT
email_input = tk.Entry(width=50)
email_input.grid(row=2,column=1,columnspan=2)
#PASS INPUT
password_input = tk.Entry(width=27)
password_input.grid(row=3,column=1,columnspan=1)


window.mainloop()