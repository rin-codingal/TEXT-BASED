from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
window = Tk()
window.title('image')
window.geometry('400x500')

# Now use Image.open to open and identify the given image file. 
limage = Image.open("one-piece.jpg")

# Convert this Image to Tkinter compatible image
image_l = ImageTk.PhotoImage(limage)

# Add image to Tkinter Label
label = Label(window, image=image_l, height=300, width=400)
button = Button(text = "Click Here", bg="white")
textbox = Text()
textbox.insert(END, "This is how you do it!")

label.pack()
button.pack()
textbox.pack()

window.mainloop()