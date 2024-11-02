import tkinter as tk
from tkinter import messagebox

def show_values():
    try:
        # Get the values from the entry boxes
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        # Show the values in a messagebox (or you can use other operations)
        messagebox.showinfo("Values", f"Value 1: {value1}\nValue 2: {value2}")
    except ValueError:
        # Handle case where input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main application window
root = tk.Tk()
root.title("Number Input UI")

# Create a frame to hold the widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)  # Make sure the frame itself is packed into the root window

# Create labels and entry boxes for the numbers
label1 = tk.Label(frame, text="Enter number 1:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Enter number 2:")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Button to display the entered values
submit_button = tk.Button(frame, text="Show Values", command=show_values)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()