import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

a_label = ttk.Label(win, text='A label')

a_label.grid(column=0, row=0)


def click_me():
    action.configure(text="*** I have been clicked ***")
    a_label.configure(foreground='red')
    a_label.configure(text="A red label")

action = ttk.Button(win, text='CLick me!', command=click_me)
action.grid(column=1, row=0)

win.mainloop()
