import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Heartbeat Monitor Simulation")

# Canvas dimensions
canvas_width = 800
canvas_height = 500

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Initial values for hr, noise, and stress
hr = 25
noise = 25
stress = hr + noise

# Scale the initial values
def scale_noise(value):
    return float(value) * -0.4 + 490

def scale_hr(value):
    return float(value) * -2 / 7 + 3130 / 7

def scale_stress(value):
    return float(value) * -2.2 + 225

hr_scaled = scale_hr(hr)
noise_scaled = scale_noise(noise)
stress_scaled = scale_stress(stress)

# Line segments for the three types of lines
line_segments_hr = []  # Heart rate line
line_segments_noise = []  # Noise line
line_segments_stress = []  # Stress line
x_position = 0
step = 5  # Step size for each segment

# Function to draw all lines
def draw_all():
    global x_position, hr_scaled, noise_scaled, stress_scaled

    # Draw the heartbeat line
    draw_line(x_position, hr_scaled, "red", line_segments_hr)

    # Draw the noise line (with a slight vertical offset)
    draw_line(x_position, noise_scaled, "blue", line_segments_noise)

    # Determine the color of the stress line based on the stress value
    if stress < 50:
        stress_color = "green"
    elif 50 <= stress < 75:
        stress_color = "yellow"
    else:
        stress_color = "red"

    # Draw the stress line (with a different vertical offset)
    draw_line(x_position, stress_scaled, stress_color, line_segments_stress)

    # Increment the x position for drawing
    x_position += step

    # Shift the line if x_position exceeds 3/4 of the canvas width
    if x_position >= 3 * canvas_width // 4:
        shift_line_left(line_segments_hr)
        shift_line_left(line_segments_noise)
        shift_line_left(line_segments_stress)

    # Schedule the next segment to be drawn
    root.after(50, draw_all)

# Function to draw a single line segment
def draw_line(x_pos, y_pos, color, line_segments):
    global step

    # Draw the next line segment
    if line_segments:
        last_line = line_segments[-1]
        x1, y1, x2, y2 = canvas.coords(last_line)
        line_segments.append(canvas.create_line(x2, y2, x2 + step, y_pos, fill=color, width=2))
    else:
        # Start the line with the first point
        line_segments.append(canvas.create_line(x_pos, y_pos, x_pos + step, y_pos, fill=color, width=2))

# Function to shift the line segments to the left
def shift_line_left(line_segments):
    global x_position

    # Move each line segment to the left
    for line in line_segments:
        x1, y1, x2, y2 = canvas.coords(line)
        canvas.coords(line, x1 - step, y1, x2 - step, y2)

    # Remove the segments that are completely off the left edge
    while line_segments and canvas.coords(line_segments[0])[2] < 0:
        canvas.delete(line_segments.pop(0))

    # Reset x_position when it reaches the end of the canvas width
    if x_position >= canvas_width:
        x_position = 3 * canvas_width // 4

# Function to update noise
def update_noise(event):
    global noise, noise_scaled
    try:
        noise = float(entry.get())
        noise_scaled = scale_noise(noise)
        print(f"Updated noise to: {noise}, scaled: {noise_scaled}")
        update_stress()  # Call update_stress after updating noise
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to update heart rate
def update_hr(event):
    global hr, hr_scaled
    try:
        hr = float(entry2.get())
        hr_scaled = scale_hr(hr)
        print(f"Updated hr to: {hr}, scaled: {hr_scaled}")
        update_stress()  # Call update_stress after updating heart rate
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to update stress based on current hr and noise
def update_stress():
    global stress, stress_scaled, hr, noise
    stress = hr + noise
    stress_scaled = scale_stress(stress)
    print(f"Updated stress to: {stress}, scaled: {stress_scaled}")

# Create Entry widgets for input
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM)
entry.bind("<Return>", update_noise)

entry2 = tk.Entry(root)
entry2.pack(side=tk.BOTTOM)
entry2.bind("<Return>", update_hr)

# Start the animation
draw_all()

# Run the application
root.mainloop()
