from tkinter import *

# Main window

calculator_window= Tk()
calculator_window.title("Calculator")
calculator_window.geometry("260x280")

# Functions

def sum():
    a= int(entry_num1.get())
    b= int(entry_num2.get())
    result = a + b
    entry.delete(0,END)
    entry.insert(0,result)

def subtraction():
    a= int(entry_num1.get())
    b= int(entry_num2.get())
    result= a - b
    entry.delete(0,END)
    entry.insert(0,result)

def division():
    a= int(entry_num1.get())
    b= int(entry_num2.get())
    result= a / b
    entry.delete(0,END)
    entry.insert(0,result)

# Panels
data_panel= Frame(calculator_window)
button_panel= Frame(calculator_window)

# Labels and Entries
Label(data_panel,text="Numero a").grid(row=0,column=0)
Label(data_panel,text="Numero b").grid(row=1,column=0)
Label(data_panel,text="Resultado").grid(row=2,column=0)

entry_num1=Entry(data_panel,width=8)
entry_num2=Entry(data_panel,width=8)
entry=Entry(data_panel,width=8)

entry_num1.grid(row=0,column=1)
entry_num2.grid(row=1,column=1)
entry.grid(row=2,column=1)

# Buttons
Button(button_panel,width=4,text="+", command=sum).grid(row=0,column=0)
Button(button_panel,width=4,text="-", command=subtraction).grid(row=0,column=1)
Button(button_panel,width=4,text="/",command=division).grid(row=0,column=2)

# Packing panels

data_panel.pack()
button_panel.pack()

# Start main loop

calculator_window.mainloop()