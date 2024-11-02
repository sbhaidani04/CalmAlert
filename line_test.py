import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Heartbeat Monitor Simulation")

# Canvas dimensions
canvas_width = 600
canvas_height = 400

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Initial y-coordinate for the baseline
initial_y = canvas_height // 2 - 50
baseline_y = initial_y

# Create a line segment that will be updated over time
line_segments = []
x_position = 0
step = 5  # Step size for each segment

# Heartbeat pattern (simulating the y-coordinates)
heartbeat_pattern = [0, -30, -10, -40, 0, -15, 0]  # Customizable pattern

# Function to draw the heartbeat line over time
def draw_heartbeat():
    global x_position, baseline_y

    # Check if the line should be drawn continuously
    y_offset = 0
    new_y = baseline_y + y_offset

    if x_position == 0:
        # Start the line with the first point
        line_segments.append(canvas.create_line(x_position, new_y, x_position + step, new_y, fill="red", width=2))
    else:
        # Draw the next line segment
        last_line = line_segments[-1]
        x1, y1, x2, y2 = canvas.coords(last_line)
        line_segments.append(canvas.create_line(x2, y2, x2 + step, new_y, fill="red", width=2))
        print(y2)

    # Increment x position for the next segment
    x_position += step

    # Shift the line if x_position exceeds 3/4 of the canvas width
    if x_position >= 3 * canvas_width // 4:
        shift_line_left()
    

    # Schedule the next segment to be drawn
    root.after(50, draw_heartbeat)

# Function to shift the line segments to the left
def shift_line_left():
    global x_position

    # Move each line segment to the left
    for line in line_segments:
        x1, y1, x2, y2 = canvas.coords(line)
        canvas.coords(line, x1 - step, y1, x2 - step, y2)

    # Remove the segments that are completely off the left edge
    while line_segments and canvas.coords(line_segments[0])[2] < 0:
        canvas.delete(line_segments.pop(0))

    # Reset x_position when the line reaches the end of the canvas
    if x_position >= canvas_width:
        x_position = 3 * canvas_width // 4

# Function to update the baseline (new y-position) when Enter is pressed
def update_baseline(event):
    global baseline_y
    try:
        baseline_y = int(entry.get())
        print(f"Updated baseline_y to: {baseline_y}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Create an Entry widget for input
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM)

# Bind the Enter key to the update_baseline function
entry.bind("<Return>", update_baseline)

# Start the animation
draw_heartbeat()

# Run the application
root.mainloop()
