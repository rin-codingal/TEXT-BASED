from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
window = Tk()
window.title('image')
window.geometry('400x400')

# Now use Image.open to open and identify the given image file. 
upload = Image.open("one-piece.jpg")

# Convert this Image to Tkinter compatible image
image2 = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(window, image=image2, height=250, width=300)
label.place(x=50, y=20)

label2 = Label(window, text="One Piece")
label2.place(x=200, y=290)

# Run the application
window.mainloop()