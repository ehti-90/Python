import tkinter as tk

window = tk.Tk()
window.title("Miles to KM ")
window.minsize(width=300, height=200)
window.configure(padx=50,pady=50)

# Label
label = tk.Label(window,text="Miles",font=("Arial", 10))
label.grid(row=0,column=3)

#label2
label2 = tk.Label(window,text="Result = ",font=("Arial", 10))
label2.grid(row=1,column=0)

#label result
label_result = tk.Label(text="HERE",font=("Arial", 10))
label_result.grid(row=1,column=1)

#Label 4
label_4 = tk.Label(text="Km",font=("Arial", 10))
label_4.grid(row=1,column=3)


#ENTRY
inp = tk.Entry(width=10)
inp.grid(row=0, column=1)
#BUTTON
def caluculate_km():
    new  = float(inp.get())    #  Gets input from Entry
    result = round((1.60934 * new),2)
    label_result.configure(text=result)
    
calculate = tk.Button(text="Calculate",bg="green",fg="white",command=caluculate_km)
calculate.grid(row=3,column=1)


window.mainloop()