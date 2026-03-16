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

 

action = ttk.Button(win, text='Click me', command=click_me)
action.grid(column=2, row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['value'] = (1, 2, 4, 42, 100)

number_chosen.grid(column=1, row=1)
number_chosen.current(0)

ttk.Label(win, text='Choose a number:').grid(column=1, row=0)

win.mainloop()
