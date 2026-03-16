import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# a_label = ttk.Label(win, text='A label')
# a_label.grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

def click_me():
    action.configure(text="Hello " + name.get())

ttk.Label(win, text="Enter a name: ").grid(column=0, row=0)

 

action = ttk.Button(win, text='Click me!', command=click_me)
action.grid(column=1, row=1)

win.mainloop()
