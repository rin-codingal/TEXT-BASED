from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("250x250")

# Event Handler for Keypress
def handle_keypress(event):
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("The button was clicked!")

#add widgets
btn = Button(text="Click me!")
btn.pack()

# Bind click event to handle_click()
btn.bind("<Button-1>", handle_click)

window.mainloop()