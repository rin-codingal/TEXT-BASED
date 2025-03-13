from tkinter import *
import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(8):
        password += random.choice(characters)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("Password Generator")

password_entry = Entry(window, width=20)
password_entry.pack(pady=10)

window.title("Random Password Generator")
window.geometry("400x300")
Button(window, text="Generate", command=generate_password).pack(pady=10)

window.mainloop()