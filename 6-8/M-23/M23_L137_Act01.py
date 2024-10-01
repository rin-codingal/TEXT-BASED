from tkinter import *
 
# Setting up Main Window
window = Tk()
window.geometry("250x250")
window.title("main")

# Function to open New (Top Level) Window
def topwin():
	top = Toplevel()
	top.geometry("150x100")
	top.title("toplevel")
	
	# Adding a label widget to Top Window
	l2 = Label(top, text = "This is top level window")
	l2.pack()

	top.mainloop()

# Adding a label and button Widget to window (Main) Window
l = Label(window, text = "This is Main window")
btn = Button(window, text = "Click here to open top window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

window.mainloop()