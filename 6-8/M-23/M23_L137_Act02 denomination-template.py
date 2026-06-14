from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
window = Tk()
window.title("")
window.config(bg="aqua")
window.geometry("")

# Adding Image and Labels in the Main Window
upload = Image.open("")

upload = upload.resize((300, 300)) # Resize the image using resize() method
image = ImageTk.(upload)
label = Label(window, image=image, bg="light blue")
label.place(x=, y=)

label1 = Label(window,
               text="Hello, Welcome to Denomination Counter Application.",
               bg="aqua")

label1.place(relx=, y=, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

# Adding Buttons to the main window
button1 = Button(window,
                 text="Let's get started!",
                 command=,
                 bg="green",
                 fg="white")
button1.place(x=, y=)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations den_counter")
    top.config(bg="light yellow")
    top.geometry("600x350+50+50")
    

    label = Label(, text="Enter total amount", bg="light yellow")
    entry = Entry(top)
    Lbl = Label(top, text="Here are number of notes for each denomination", bg="light yellow")

    L1 = Label(top, text="", bg="light yellow")
    L2 = Label(top, text="", bg="light yellow")
    L3 = Label(top, text="", bg="light yellow")
    L4 = Label(top, text="", bg="light yellow")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def den_counter():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 
            amount %= 

            note1000 = amount // 
            amount %= 

            note500 = amount // 500
            amount %= 500

            note100 = amount // 

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note1000))
            t3.insert(END, str(note500))
            t4.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=, bg="lime", fg="black")

    # Centering Widgets in the Top Window
    label.place(x=, y=50)
    entry.place(x=, y=80)
    btn.place(x=, y=120)
    Lbl.place(x=, y=170)

    L1.place(x=180, y=)
    L2.place(x=180, y=)
    L3.place(x=180, y=)
    L4.place(x=180, y=)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)

    top.mainloop()

window.mainloop()