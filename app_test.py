import tkinter as tk
from tkinter import messagebox
import math
import random

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.baseHeartRate = None
        self.baseHearing = None
        self.title("Calm Alert")

        # Container to hold all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to store references to each page
        self.pages = {}
        
        # Add pages to the container
        for Page in (StartPage, HeartbeatSimulation):
            page_name = Page.__name__
            page = Page(parent=container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the start page initially
        self.show_page("StartPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        button2 = tk.Button(self, text="Open Heartbeat Simulation", 
                            command=lambda: controller.show_page("HeartbeatSimulation"))
        button2.pack()

        # Create a frame to hold the widgets
        label = tk.Label(self, text="Input Base Values")
        label.pack(pady=3, padx=10)

        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        # Create labels and entry boxes for the numbers
        self.label1 = tk.Label(self.frame, text="Enter Heart Rate:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(self.frame, text="Enter Noise Level:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # Button to display the entered values
        submit_button = tk.Button(self.frame, text="Submit", command=self.pass_values)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def pass_values(self):
        try:
            # Get the values from the entry boxes
            value1 = float(self.entry1.get())
            value2 = float(self.entry2.get())
            self.controller.pages["HeartbeatSimulation"].set_initial_values(value1, value2)
            # Show the values in a messagebox (or you can use other operations)
            messagebox.showinfo("Values", f"Heart Rate: {value1}\nNoise Level: {value2}")
        except ValueError:
            # Handle case where input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter valid numbers")

class HeartbeatSimulation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initial hr and noise values
        self.hr = 25  # default value
        self.noise = 25  # default value
        self.stress = self.hr + self.noise
        self.normalHRMin = 60
        self.normalHRMax = 100
        self.normalHRAvg = int((self.normalHRMin + self.normalHRMax) / 2) # average of the 2 min and max

        # Stressed hr and noise values
        self.stressHRMin = 150
        self.stressHRMax = 220
        self.stressHRAvg = int((self.normalHRMin + self.stressHRMax) / 2) # average of the normal min and stress max

        # Canvas setup
        self.canvas_width = 800
        self.canvas_height = 500
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Entry widgets for updating hr and noise
        self.entry_hr = tk.Entry(self)
        self.entry_hr.pack(side=tk.BOTTOM)
        self.entry_hr.bind("<Return>", self.update_hr)

        self.entry_noise = tk.Entry(self)
        self.entry_noise.pack(side=tk.BOTTOM)
        self.entry_noise.bind("<Return>", self.update_noise)

        # Line segments for the three types of lines
        self.line_segments_hr = []  # Heart rate line
        self.line_segments_noise = []  # Noise line
        self.line_segments_stress = []  # Stress line
        self.x_position = 0
        self.step = 5  # Step size for each segment

        # Back button
        button = tk.Button(self, text="Back to Start Page", command=lambda: controller.show_page("StartPage"))
        button.pack()

    def set_initial_values(self, hr, noise, stress):
        """Sets the initial hr and noise values and starts the animation."""
        self.hr = hr
        self.noise = noise
        self.stress = self.hr + self.noise
        print(f"Starting HR: {self.hr}, Noise: {self.noise}")

        # Scale the initial values
        self.hr_scaled = self.scale_hr(self.hr)
        self.noise_scaled = self.scale_noise(self.noise)
        self.stress_scaled = self.scale_stress(self.stress)

        # Clear any existing lines
        self.canvas.delete("all")
        self.line_segments_hr.clear()
        self.line_segments_noise.clear()
        self.line_segments_stress.clear()
        self.x_position = 0

        # Start the animation
        self.draw_all()
    

    def scale_noise(self, value):
        return float(value) * -0.4 + 490

    def scale_hr(self, value):
        return float(value) * -2 / 7 + 3130 / 7

    def scale_stress(self, value):
        return float(value) * -2.2 + 225
    
    def normalHRGenerator(self, pastVal):
        if (pastVal == self.normalHRMin | pastVal == (self.normalHRMin + 3) | pastVal == (self.normalHRMin - 3)): # if pastVal equals the min, then generate value slightly higher than min but <= avg
            self.normalHR = random.randint(self.normalHRMin + 3, self.normalHRAvg)
        elif (pastVal == self.normalHRAvg): # if pastVAL equal to the peak, then generate value slightly higher than avg but <= max 
            normalHR = random.randint(self.normalHRAvg + 3, self.normalHRMax)
        elif (pastVal == self.normalHRMax | pastVal == (self.normalHRMax + 3) | pastVal == (self.normalHRMax - 3)): # if pastVal approx. equals the max, then generate value slightly lower than max but <= avg
            normalHR = random.randint(self.normalHRAvg, self.normalHRMax -3)
        elif (self.normalHRMin < pastVal < self.normalHRAvg): # if pastVal bless than peak, then generate value slightly higher than pastVal but <= avg
            if (pastVal + 3 <= self.normalHRAvg):
                normalHR = random.randint(pastVal + 3, self.normalHRAvg)
            else:
                normalHR = random.randint(self.normalHRAvg + 3, self.normalHRMax)
        elif (self.normalHRAvg < pastVal < self.normalHRMax): # if pastVal greater than peak, then generate value slightly higher than pastVal but <= max
            if (pastVal + 3 <= self.normalHRMax):
                normalHR = random.randint(pastVal + 3, self.normalHRMax)
            else:
                normalHR = random.randint(self.normalHRAvg, pastVal)
        else:
            normalHR = random.randint(self.normalHRMin, self.normalHRMax)    
        return normalHR

    def draw_all(self):

        # Draw the heartbeat line
        self.draw_line(self.x_position, self.hr_scaled, "red", self.line_segments_hr)

        # Draw the noise line (with a slight vertical offset)
        self.draw_line(self.x_position, self.noise_scaled, "blue", self.line_segments_noise)

        # Determine the color of the stress line based on the stress value
        if self.stress < 50:
            stress_color = "green"
        elif 50 <= self.stress < 100:
            stress_color = "yellow"
        else:
            stress_color = "red"

        # Draw the stress line (with a different vertical offset)
        self.draw_line(self.x_position, self.stress_scaled, stress_color, self.line_segments_stress)

        # Increment the x position for drawing
        self.x_position += self.step

        # Shift the line if x_position exceeds 3/4 of the canvas width
        if self.x_position >= 3 * self.canvas_width // 4:
            self.shift_line_left(self.line_segments_hr)
            self.shift_line_left(self.line_segments_noise)
            self.shift_line_left(self.line_segments_stress)

        # Schedule the next segment to be drawn
        self.after(50, self.draw_all)

    def draw_line(self, x_pos, y_pos, color, line_segments):
        # Draw the next line segment
        if line_segments:
            last_line = line_segments[-1]
            x1, y1, x2, y2 = self.canvas.coords(last_line)
            line = self.canvas.create_line(x2, y2, x2 + self.step, y_pos, fill=color, width=2)
            line_segments.append(line)
        else:
            # Start the line with the first point
            line = self.canvas.create_line(x_pos, y_pos, x_pos + self.step, y_pos, fill=color, width=2)
            line_segments.append(line)

    def shift_line_left(self, line_segments):
        # Move each line segment to the left
        for line in line_segments:
            x1, y1, x2, y2 = self.canvas.coords(line)
            self.canvas.coords(line, x1 - self.step, y1, x2 - self.step, y2)

        # Remove the segments that are completely off the left edge
        while line_segments and self.canvas.coords(line_segments[0])[2] < 0:
            self.canvas.delete(line_segments.pop(0))

        # Reset x_position when it reaches the end of the canvas width
        if self.x_position >= self.canvas_width:
            self.x_position = 3 * self.canvas_width // 4

    def update_noise(self, event):
        try:
            self.noise = float(self.entry_noise.get())
            self.noise_scaled = self.scale_noise(self.noise)
            print(f"Updated noise to: {self.noise}, scaled: {self.noise_scaled}")
            self.update_stress()  # Call update_stress after updating noise
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update_hr(self, event):
        try:
            self.hr = float(self.entry_hr.get())
            self.hr_scaled = self.scale_hr(self.hr)
            print(f"Updated hr to: {self.hr}, scaled: {self.hr_scaled}")
            self.update_stress()  # Call update_stress after updating heart rate
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update_stress(self):
        self.stress = self.hr + self.noise
        self.stress_scaled = self.scale_stress(self.stress)
        print(f"Updated stress to: {self.stress}, scaled: {self.stress_scaled}")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
