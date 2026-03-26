import customtkinter as ctk

def button_calback():
    print("button clicked")


app = ctk.CTk()
app.geometry("400x150")

ctk.set_appearance_mode('dark')


button = ctk.CTkButton(app, text="Button", command=button_calback)
button.pack(padx=20, pady=20)


app.mainloop()
