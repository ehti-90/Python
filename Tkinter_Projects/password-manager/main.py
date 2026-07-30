import tkinter as tk
from tkinter import messagebox
import password_gen
import pyperclip
import json


# ----------------------------  Search our Datafile ------------------------------- #

def search_me():
    search_website = web_input.get()
   
    
    try:
        with open(file=r"practice projects\Tkinter_Projects\password-manager\password.json",mode="r") as file:
            dictionary_data = json.load(file)
        
    except (FileNotFoundError,json.JSONDecodeError):
        messagebox.showerror(message="No DataFile Found")
    else:
            if search_website in dictionary_data:
                messagebox.showinfo(title=f"{search_website}", message=f"email: {dictionary_data[search_website]["email"]}\n password: {dictionary_data[search_website]["password"]}")
            else:
                 messagebox.showinfo(title=f"{search_website}", message="Does not exist in Datafile")
                
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    my_password = password_gen.generate()

    password_input.delete(0,"end")  # Delete everything previous when clicked again # if we dont like it it will generate a new one                            
    pyperclip.copy(my_password)     # Directly copied to our clipboard You can past it on go.   
    password_input.insert(0, my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    
    web = web_input.get() # .get gives us the input from the entry
    pas = password_input.get()
    email = email_input.get()
    
    new_data = {
        web:{
            "email":email,
            "password":pas
        }
        }
    
    
    if len(web) == 0 or len(pas) == 0:
        retry = messagebox.showinfo(title="Error", message="Fill the Entries")
    
    else:  
        try:      
            with open(file=r"practice projects\Tkinter_Projects\password-manager\password.json",mode="r") as data:
                file_data = json.load(data)  #   reading old data to data var
                 
                
        except (FileNotFoundError, json.JSONDecodeError):
            file_data = {}
            file_data.update(new_data)
            with open(file=r"practice projects\Tkinter_Projects\password-manager\password.json",mode="w") as file:
                json.dump(file_data,file,indent=4) 
        else:
            file_data.update(new_data)# if file not found or empty make dict and update the dictionary
                
            with open(file=r"practice projects\Tkinter_Projects\password-manager\password.json",mode="w") as file:
                json.dump(file_data,file,indent=4) # load json into file
                
        finally:  
            web_input.delete(0, "end")
            password_input.delete(0, "end") #Deletes the input we gave after clicking add button
            web_input.focus()
    
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=700,height=500)
window.config(padx=80,pady=80,bg="Black")



#Canvas 
canvas = tk.Canvas(width=200,height=200,bg="black",highlightthickness=0)
lock_image = tk.PhotoImage(file=r"practice projects\Tkinter_Projects\password-manager\logo.png")
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
add_butt = tk.Button(text="ADD",width=44,bg="#212830",fg="white",command=save_to_file)
add_butt.grid(row=4,column=1,columnspan=2)

#GENERATE BUTTON
generate_pass = tk.Button(text="  Generate ",padx=10,bg="#2e9a40",command=generate_password)
generate_pass.grid(row=3,column=2,columnspan=3)

#SEARCH BUTTON
search_button = tk.Button(text="  Search ",padx=15,bg="yellow",fg="black",command=search_me)
search_button.grid(row=1,column=2,columnspan=2)

# WEB ENTRY
web_input = tk.Entry(width=38)
web_input.focus()
web_input.grid(row=1,column=1,columnspan=1)
#EMAIL ENTRY
email_input = tk.Entry(width=53)
email_input.insert(0, "dummy69@gmail.com") # my common most email
email_input.grid(row=2,column=1,columnspan=2)
#PASSWORD ENTRY
password_input = tk.Entry(width=38)
password_input.grid(row=3,column=1)


window.mainloop()