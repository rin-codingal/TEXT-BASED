from tkinter import *
from datetime import date

# Create Window
window = Tk()
window.title("Here's The Product")
window.geometry("400x300")

# Function to calculate the product
def multiply():
	n1 = int(n1_entry.get())
	n2 = int(n2_entry.get())
	
	product = n1*n2
	
	result.insert(END, "Here's the result\n")
	result.insert(END, product)

# add the widgets
lbl = Label(text="Let's Multiply Two Numbers", fg="yellow", bg="red", height=1, width=300) #title

n1_lbl = Label(text="Enter First Number", bg="lime")
n1_entry = Entry()

n2_lbl = Label(text="Enter Second Number", bg="lime")
n2_entry = Entry()

result = Text(height=3)

btn = Button(text="Calculate", command=multiply, height=1, bg="#1261A0", fg="white")

# Organize the widgets
lbl.pack()

n1_lbl.pack()
n1_entry.pack()

n2_lbl.pack()
n2_entry.pack()

btn.pack()
result.pack()

window.mainloop()