from tkinter import *

#creating window
window = Tk()
window.title("Tkinter Sample Window")
window.geometry("400x300") #width = 400, height = 300

# Label
greeting = Label(text="Hello I am label", fg="black", bg="white")

# Button 
button = Button(text="Click me, I am a button", bg="black", fg="yellow")

# Entry 
entry = Entry(fg="white", bg="red", width=30)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="Sample Frame")
label.pack()

textbox = Text(fg="green", bg="orange")
textbox.pack()

window.mainloop()