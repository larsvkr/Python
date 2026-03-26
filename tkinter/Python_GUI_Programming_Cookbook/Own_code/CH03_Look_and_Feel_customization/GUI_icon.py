import tkinter as tk
from PIL import ImageTk, Image 


win = tk.Tk()
win.title("Python GUI")


canvas = tk.Canvas(win, width=300, height=300)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("Untitled.png"))
canvas.create_image(20,20, anchor=tk.NW, image=img)

win.iconbitmap("@Untitled.xbm")
win.mainloop()