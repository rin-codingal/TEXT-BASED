from tkinter import *
 
# Setting up Main Window
window = Tk()
window.geometry("400x300")
window.title("Top a Window")

# Function to open New (Top Level) Window
def topwin():
	# Setting up Top Window
	top = Toplevel()
	top.geometry("250x100")
	top.title("toplevel")
	
	# Adding a label widget to Top Window
	l2 = Label(top, text = "This is toplevel window")
	l2.pack()

	top.mainloop()

# Adding a label and button Widget to window (Main) Window
l = Label(window, text = "This is main window")
btn = Button(window, text = "Click here to open another window", bg="yellow", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

window.mainloop()
