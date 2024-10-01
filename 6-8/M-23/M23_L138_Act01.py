from tkinter import *
import random
import time

window = Tk()
window.title('Restaurant Management System')
window.geometry("700x400")
localtime=time.asctime(time.localtime(time.time()))

def insert():
	val_order.delete(0,END)
	val_order.insert(END, str(random.randint(0, 1000)))

#add the widgets and arrange them
f1 = Frame(window,width = 350,height=200,relief=SUNKEN)
f1.place(x=0, y=200)

f2 = Frame(window ,width = 350,height=200,relief=SUNKEN)
f2.pack(side=RIGHT)

lblinfo = Label(window, font=( 'aria' ,15, 'bold' ),text="Sanctuary Kitchen Billing System",fg="blue",bd=10)
lblinfo.place(x=150, y=0)

lbl_info = Label(window, font=( 'aria' ,10, ),text=localtime,fg="blue")
lbl_info.place(x=250, y=40)

lbl_order = Label(window, text="Order Number")
lbl_order.place(x=200, y=70)

val_order = Entry(window)
val_order.place(x=310, y=70)

btn_order = Button(text="New Order", bg="lime", width=10, command=insert)
btn_order.place(x=100, y=65)

window.mainloop()