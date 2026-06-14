import random, string
from tkinter import *

# Create Window
window = Tk()
window.title("Password generator")
window.geometry("400x400")

#input the length of password
#length = int(input("Enter the length of password: "))             

def generate_passwd():
    pwdLength = int(pwdlength_entry.get()) #getting the desired password length

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    #combine the data
    all = lower + upper + num + symbols

    #use random 
    temp = random.sample(all,pwdLength)

    #create the password 
    password = "".join(temp)

    lbl_pwd["text"] = password

#print the password
#print("your random password is: "+password)


#create widgets
frame = Frame(master=window, height=150, width=360, bg="#00ffff")

lbl1 = Label(frame, text="Password Length", bg="green", fg="white", width=12)
lbl2 = Label(frame, text="Your Password is", bg="green", fg="white", width=12)

pwdlength_entry = Entry(frame)
lbl_pwd = Label(frame, bg="white", fg="black", width=20)

res = Text(bg="white", fg="black")

btn = Button(text="Create Password", command=generate_passwd, bg="white", fg="black")

# Arrange all widgets
frame.place(x=20, y=0)

lbl1.place(x=20, y=20)
pwdlength_entry.place(x=150, y=20)

lbl2.place(x=20, y=80)
lbl_pwd.place(x=150, y=80)

btn.place(x=130, y=210)

res.place(y=250)

window.mainloop()