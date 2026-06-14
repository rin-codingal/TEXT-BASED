from tkinter import *
import random

window = Tk()
window.title("Game")
window.geometry("400x300")
#frame = Frame(window)
#frame.pack()

RockL = Label(text="     Rock     ", bg="Gray", fg="White", height=2, width=10, font=10)
Paper = Label(window, text="     Paper     ", bg="Gray", fg="White", height=2, width=10, font=10)
Scisor = Label(window, text="     Scisor     ", bg="Gray", fg="White", height=2, width=10, font=10)

Button1 = Button(window, bg="Gray", height=1, width=5)
Button2 = Button(window, bg="Gray", height=1, width=5)
Button3 = Button(window, bg="Gray", height=1, width=5)
RestartButton = Button(window, text="     Restart     ", bg="Gray", fg="White", height=2, width=10)

#RockL.pack()
RockL.grid(row=0, column=0, padx=5, pady=5)
Paper.grid(row=0, column=1, padx=5, pady=5)
Scisor.grid(row=0, column=2, padx=5, pady=5)

Button1.grid(row=1, column=0, padx=5, pady=5)
Button2.grid(row=1, column=1, padx=5, pady=5)
Button3.grid(row=1, column=2, padx=5, pady=5)
RestartButton.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()