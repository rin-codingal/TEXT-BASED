from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
window = Tk()
window.title("Denomination Counter")
window.config(bg="aqua")
window.geometry("650x400")

# Adding Image and Labels in the Main Window
upload = Image.open("app-image.jpeg")

upload = upload.resize((300, 300)) # Resize the image using resize() method
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(window,
               text="Hello, Welcome to Denomination Counter Application.",
               bg="aqua")

label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

# Adding Buttons to the main window
button1 = Button(window,
                 text="Let's get started!",
                 command=msg,
                 bg="green",
                 fg="white")
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations den_counter")
    top.config(bg="light yellow")
    top.geometry("600x350+50+50")
    

    label = Label(top, text="Enter total amount", bg="light yellow")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light yellow")

    l1 = Label(top, text="2000", bg="light yellow")
    l2 = Label(top, text="1000", bg="light yellow")
    l3 = Label(top, text="500", bg="light yellow")
    l4 = Label(top, text="100", bg="light yellow")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def den_counter():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000

            note1000 = amount // 1000
            amount %= 1000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

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

    btn = Button(top, text="Calculate", command=den_counter, bg="lime", fg="black")

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)

    top.mainloop()

window.mainloop()