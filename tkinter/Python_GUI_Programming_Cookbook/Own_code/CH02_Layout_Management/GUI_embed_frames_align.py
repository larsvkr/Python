import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

colors = ["Blue", "Gold", "Red"]
scrol_w = 50
scrol_h = 3


win = tk.Tk()
win.title("Python GUI")

mighty = ttk.LabelFrame(win, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)


# a_label = ttk.Label(win, text='A label')
# a_label.grid(column=0, row=0)
def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0,row=6, columnspan=3)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

radVar = tk.IntVar()
#Using a loop for the radiobuttons
for col in range(3):
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)
# rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
# rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
# rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)

# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)


def click_me():
    action.configure(text="Hello " + name.get() + ' ' +
    number_chosen.get())


ttk.Label(mighty, text="Enter a name: ").grid(column=0, row=0)
ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)

action = ttk.Button(mighty, text='Click me', command=click_me)
action.grid(column=2, row=1)

number_chosen.grid(column=1, row=1)
number_chosen.current(0)

buttons_frame = ttk.LabelFrame(mighty, text='Labels in a Frame ')
buttons_frame.grid(column=0, row=7)
#buttons_frame.grid(column=1, row=7)

ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label2').grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label3').grid(column=2, row=0, sticky=tk.W)

for child in mighty.winfo_children():
    child.grid_configure(sticky='NSWE')



win.mainloop()
