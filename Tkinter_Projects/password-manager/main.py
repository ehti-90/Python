import tkinter as tk
from tkinter import messagebox
import password_gen

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    my_password = password_gen.generate()

    password_input.delete(0,"end")  # Delete everything previous when clicked again 
    print(my_password)              # if we dont like it it will generate a new one
    password_input.insert(0, my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    
    web = web_input.get() # .get gives us the input from the entry
    pas = password_input.get()
    email = email_input.get()
    
    
    
    if len(web) == 0 or len(pas) == 0:
        retry = messagebox.showinfo(title="Error", message="Fill the Entries")
    
    else:
        confirmation = messagebox.askokcancel(title="Confirmation",message=f"Website : {web}\n Password  : {pas}\n Email : {email}\n Are You Sure ?")

        if confirmation:
            
            with open(file="password.txt",mode="a") as data:
                data.write(f"{web} | {email} | {pas}\n")
                web_input.delete(0, "end")
                password_input.delete(0, "end") #Deletes the input we gave after clicking add button
                
    
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=700,height=500)
window.config(padx=80,pady=80,bg="Black")



#Canvas 
canvas = tk.Canvas(width=200,height=200,bg="black",highlightthickness=0)
lock_image = tk.PhotoImage(file="practice projects\Tkinter_Projects\password-manager\logo.png")
canvas.create_image(140,100,image=lock_image) # x and y on canvas
canvas.grid(row=0,column=1)


#WEBSITE LABEL
web_label = tk.Label(text="Website :",bg="black",fg="white")
web_label.grid(row=1,column=0)
#EMAIL LABEL
email_label = tk.Label(text="Email :",bg="black",fg="white")
email_label.grid(row=2,column=0)
#PASSWORD LABEL
pass_label = tk.Label(text="Password : ",bg="black",fg="white")
pass_label.grid(row=3,column=0)


#ADD BUTTON
add_butt = tk.Button(text="ADD",width=44,bg="green",command=save_to_file)
add_butt.grid(row=4,column=1,columnspan=2)

#GENERATE BUTTON
generate_pass = tk.Button(text="  Generate ",padx=10,bg="yellow",command=generate_password)
generate_pass.grid(row=3,column=2,columnspan=3)


# WEB ENTRY
web_input = tk.Entry(width=53)
web_input.focus()
web_input.grid(row=1,column=1,columnspan=2)
#EMAIL ENTRY
email_input = tk.Entry(width=53)
email_input.insert(0, "ehtishamhassan396@gmail.com") # my common most email
email_input.grid(row=2,column=1,columnspan=2)
#PASSWORD ENTRY
password_input = tk.Entry(width=38)
password_input.grid(row=3,column=1)


window.mainloop()