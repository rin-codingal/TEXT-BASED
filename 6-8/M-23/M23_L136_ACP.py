from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("My Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)



# Function to Save a file
def save_file():  
    # Save the current file as a new file  
    filepath = asksaveasfilename(
                                defaultextension="txt",
                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                                ) 
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:	
        fname = name_entry.get()	 
        address = address_entry.get()
        text = f"Name: {fname}\nAddress: {address}"
        output_file.write(text) # update in the output file

    window.title(f"My Text Editor - {filepath}")

# create widgets
frame = Frame(master=window, height=200, width=360, bg="#00ffff")

lbl1 = Label(frame, text="Full Name", bg="green", fg="white", width=12)
lbl2 = Label(frame, text="Address", bg="green", fg="white", width=12)

name_entry = Entry(frame)
address_entry = Entry(frame)


res = Text(bg="white", fg="black")

btn_save = Button(text="Save", command=save_file, bg="green", fg="yellow")

# Arrange all widgets
frame.place(x=20, y=0)

lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x=20, y=80)
address_entry.place(x=150, y=80)

btn_save.place(x=130, y=210)

res.place(y=250)

window.mainloop()