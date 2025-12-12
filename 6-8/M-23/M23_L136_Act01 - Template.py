from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("")
window.geometry("") #width = 600, height = 500
window.rowconfigure(0, minsize=, weight=1)
window.columnconfigure(1, minsize=, weight=1)

# Function to Open a file
def open_file():	
    #open file
	filepath = askopenfilename(filetypes=[("", "*."), ("", "*.*")])
      
	if not filepath:
		return
      
	txt_edit.delete(1.0, END)
      
	# if a file is opened then display the contents of the file
	with open(, "r") as input_file:		
		text = input_file.() # Read contents of the input file            
		
		txt_edit.insert(END, ) # Insert contents of the file in the editor box
            
		input_file.()
	window.title(f" - {filepath}")

# Function to Save a file
def save_file():  
    # Save the current file as a new file  
    filepath = asksaveasfilename(
                                defaultextension="",
                                filetypes=[("", "*."), ("", "*.*")]
                                ) 
    if not filepath:
        return
    
    with open(filepath, "") as output_file:		 
        text = txt_edit.get(1.0, END) # Read the edited content
        output_file.write(text) # update in the output file

    window.title(f" - {filepath}")

# create widgets
txt_edit = Text()
fr_buttons = Frame(, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="", command=)
btn_save = Button(fr_buttons, text="...", command=)

# arrange the widgets
btn_open.grid(row=, column=, sticky="", padx=, pady=)
btn_save.grid(row=, column=, sticky="", padx=)

fr_buttons.grid(row=, column=, sticky="")
txt_edit.grid(row=, column=, sticky="")

window.mainloop()