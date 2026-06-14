from tkinter import *

window = Tk()
window.title("Login App")
window.geometry("400x300")

def display():
	name = name_entry.get()
	greet = "Hey "+name+"!"
	message =  "\nCongratulations for your new account!"
	textbox.insert(END, greet)
	textbox.insert(END, message)

#add the widgets
label1 = Label(text = "Enter Full Name", bg="red")
label2 = Label(text = "Email Id", bg="red")
label3 = Label(text = "Enter Password", bg="red")

name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text = "Create Account", command=display)

# Arrange all widgets
label1.pack()
name_entry.pack()

label2.pack()
email_entry.pack()

label3.pack()
pass_entry.pack()

btn.pack()
textbox.pack()

window.mainloop()