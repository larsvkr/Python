import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext

colors = ["Blue", "Gold", "Red"]
scrol_w = 50
scrol_h = 3

def radCall():
    radSel = radVar.get()
    if radSel == 0: mighty2.configure(text='Blue')
    elif radSel == 1: mighty2.configure(text='Gold')
    elif radSel == 2: mighty2.configure(text='Red')


win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Tab 1")
tabControl.add(tab2, text="Tab 2")

tabControl.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text="Mighty Python ")
mighty.grid(column=0, row=0, padx=8, pady=4)

mighty2 = ttk.LabelFrame(tab2, text="The Snake ")
mighty2.grid(column=0, row=0, padx=8, pady=4)

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()


number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)

def click_me():
    action.configure(text="Hello " + name.get() + ' ' +
    number_chosen.get())


ttk.Label(mighty, text="Enter a name: ").grid(column=0, row=0)
ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)

action = ttk.Button(mighty, text='Click me', command=click_me)
action.grid(column=2, row=1)

chVarDis = tk.IntVar()
check_1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled' )
check_1.grid(column=0, row=4)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

radVar = tk.IntVar()
#Using a loop for the radiobuttons
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0,row=6, columnspan=3)

ttk.Label(mighty, text=" Choose a number:").grid(column=1, row=0)


buttons_frame = ttk.LabelFrame(mighty2, text='Labels in a Frame')
buttons_frame.grid(column=0, row=7, padx=8, pady=4)

ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label2').grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label3').grid(column=2, row=0, sticky=tk.W)

for child in mighty.winfo_children():
    child.grid_configure(padx=8)

win.mainloop()