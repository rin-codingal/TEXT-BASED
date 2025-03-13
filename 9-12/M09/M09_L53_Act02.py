from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
window = Tk()
window.title("Message Box")
window.geometry("200x200")

# Function for Displaying Warning Message
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(window, text="Scan for Virus",fg="blue",bg="yellow", command=msg)
button.place(x=50, y=80)

# Entering main event loop
window.mainloop()