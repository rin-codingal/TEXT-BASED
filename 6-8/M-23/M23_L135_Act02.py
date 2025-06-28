from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
window = Tk()
window.geometry("250x250")
window.title("Virus Detected")

def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")

#add widgets
btn = Button(window, text="Scan for Virus", command=msg)
btn.place(x=75, y=80)


window.mainloop()