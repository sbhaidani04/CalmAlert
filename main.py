import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Adjustable Line with Input Box")

# Canvas dimensions
canvas_width = 600
canvas_height = 400

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Initial y-coordinate for the line
initial_y = canvas_height / 2
line = canvas.create_line(0, initial_y, canvas_width / 2, initial_y, fill="red", width=2)

# Function to update the line's position
def update_line():
    y = int(spinbox.get())
    # Update the line's coordinates
    canvas.coords(line, 0, y, canvas_width / 2, y)

# Create a Spinbox widget for input (with arrows to increase/decrease the value)
spinbox = tk.Spinbox(root, from_=0, to=canvas_height, command=update_line)
spinbox.set(initial_y)
spinbox.pack(side=tk.BOTTOM, fill=tk.X)

# Run the application
root.mainloop()
