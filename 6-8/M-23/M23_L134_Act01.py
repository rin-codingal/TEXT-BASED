from tkinter import *

window = Tk()
window.title("Number Pad")
window.geometry("250x300")

# Create the number grid
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]

# Configure rows and columns to resize window
for i in range(4):
	window.columnconfigure(i, weight=1, minsize=75)
	window.rowconfigure(i, weight=1, minsize=50)
	

for i in range(4):
	for j in range(3):
		frame = Frame(
			master=window,
			relief=SUNKEN,
			borderwidth=1,
			bg="red"
		)
		
		frame.grid(row=i, column=j, sticky="nsew")

		label = Label(master=frame, text=nums[i][j], bg="lime", font=("Arial", 18))
		label.pack(expand=True, fill="both", padx=5, pady=5)

window.mainloop()
