from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def MSG():
    msg_box = messagebox.showinfo("Alert", "Do you want to Calculate the denomination Count ?")
     
    if msg_box == "ok":
        TopWin()

def TopWin():
    # Creating the Second Window
    Top = Toplevel()
    Top.title("Denomination Counter")
    Top.geometry("650x400")

    # Function to Calculate the denomination
    def den_counter():
        try:
            global amount
            amount = int(Entry1.get())

            note2000 = amount // 2000 
            amount = amount % 2000

            note1000 = amount // 1000
            amount = amount % 1000

            note500 = amount // 500
            amount = amount % 500

            note100 = amount // 100
            
            # Clearing the previous result
            Entry2.delete(0, END)
            Entry3.delete(0, END)
            Entry4.delete(0, END)
            Entry5.delete(0, END)

            # Dusplaying the current result
            Entry2.insert(END, str(note2000))
            Entry3.insert(END, str(note1000))
            Entry4.insert(END, str(note500))
            Entry5.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("ERROR", "Please entrer a Valide Number !")

    # Creating Widget for the Second Window
    Label3 = Label(Top, text="Enter the total Amount")
    Entry1 = Entry(Top)
    Label4 = Label(Top, text="Here are number of Notes for each Denomination")

    Label5 = Label(Top, text="2000")
    Label6 = Label(Top, text="1000")
    Label7 = Label(Top, text="500")
    Label8 = Label(Top, text="100")

    Entry2 = Entry(Top)
    Entry3 = Entry(Top)
    Entry4 = Entry(Top)
    Entry5 = Entry(Top)

    Button2 = Button(Top, text="Calculate", command=den_counter)

    # Displaying the widget on the second window
    Label3.place(x=230, y=50)
    Entry1.place(x=200, y=80)
    Button2.place(x=240, y=120)
    Label4.place(x=140, y=170)
    Label5.place(x=180, y=200)
    Label6.place(x=180, y=230)
    Label7.place(x=180, y=260)
    Label8.place(x=180, y=290)
    Entry2.place(x=270, y=200)
    Entry3.place(x=270, y=230)
    Entry4.place(x=270, y=260)
    Entry5.place(x=270, y=290)

    Top.mainloop()


# Setting up the main window
window = Tk()
window.geometry("650x400")
window.title("Denomination Calculator")

# Opening the Image
Upload = Image.open("images.jpg")
Upload = Upload.resize((300, 300))

# Converting into Compatible image
img = ImageTk.PhotoImage(Upload)

# Creating Widgets
Label1 = Label(window, image=img)
Label2 = Label(window, text="Welcome to the denomination Calculator")
Button1 = Button(window, text="Let's Get Started", command=MSG)

# Displaying the Widgets
Label1.place(x=180, y=20)
Label2.place(relx=0.5, y=340, anchor=CENTER)
Button1.place(x=260, y=360)

window.mainloop()