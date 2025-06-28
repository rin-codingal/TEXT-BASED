# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox

# Define the RestaurantManagementApp class
class RestaurantOrderManagement:
    # Initialize the application
    def __init__(self, root):
        self.root = root  # The main window of the app
        self.root.title(
            "")  # Set the title of the window

        # A dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # Exchange rate for currency conversion

        self.setup_background(root)  # Set up the background image

        # Create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place()  # Place it at the center of the window

        # Heading label
        ttk.Label(frame,
                  text="",
                  font=("", 20, "")).grid(row=0,
                                                   columnspan=3,
                                                   padx=10,
                                                   pady=10)

        self.menu_labels = {}  # To store references to menu item labels
        self.menu_quantities = {}  # To store references to quantity entry widgets

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,
                              text=f"{} (${}):",
                              font=("", 12))
            label.grid(row=i, column=, padx=, pady=)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=)
            quantity_entry.grid(row=i, column=, padx=, pady=)
            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="",
                  font=("", 12)).grid(row=len(self.menu_items) + 1,
                                           column=,
                                           padx=,
                                           pady=)

        # Dropdown for currency selection
        currency_dropdown = ttk.Combobox(frame,
                                         textvariable=self.currency_var,
                                         state="",
                                         width=,
                                         values=('USD', 'INR'))
        currency_dropdown.grid(row=len(self.menu_items) + 1,
                               column=1,
                               padx=10,
                               pady=5)
        currency_dropdown.current(0)  # Set default currency

        # Update prices when currency changes
        self.currency_var.trace('w',self.update_menu_prices)  

        # Button to place the order
        order_button = ttk.Button(frame,
                                  text="",
                                  command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,
                          columnspan=,
                          padx=,
                          pady=)

    # Method to set up the background image
    def setup_background(self, root):
        bg_width, bg_height = 
        canvas = tk.Canvas(root, width=, height=)
        canvas.pack()
        original_image = tk.PhotoImage(file="")
        background_image = original_image.subsample(
            original_image.width() // bg_width,
            original_image.height() // bg_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image

    # Method to update the menu prices based on the selected currency
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    # Method to place an order
    def place_order(self):
        total_cost = 0
        order_summary = ""
        currency = 
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, entry in self.menu_quantities.items():
            quantity = 
            if quantity.isdigit():
                quantity = 
                price = 
                cost = 
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{}: {} x {symbol}{} = {symbol}{}\n"
        if total_cost > 0:
            order_summary += f"\n {}{}"
            messagebox.showinfo(
                "",
                order_summary)  # Show order summary in a message box
        else:
            # Show error if no items are ordered
            messagebox.showerror("", "")  


# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("")  # Set the size of the window
    root.mainloop()  # Start the GUI loop
