import tkinter as tk

# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("250x75")
window.resizable(width=False, height=False)

def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

#create widgets
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
label_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

btn_convert = tk.Button(master=window, text="-->", command=fahrenheit_to_celsius)
label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# arrange the widgets
frm_entry.grid(row=0, column=0, padx=10)
ent_temperature.grid(row=0, column=0, sticky="e")
label_temp.grid(row=0, column=1, sticky="w")
btn_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=2, padx=10)

window.mainloop()