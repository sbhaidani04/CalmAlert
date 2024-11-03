import tkinter as tk
from tkinter import messagebox
from stress_algorithm import overall_stress_level
from randomHRGen import normalHRGenerator, stressHRGenerator
from decibel_random_variation import normal_decibel_variation, stressed_decibel_variation

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
                            command=self.start_sim)
        button2.pack()

        # Create a frame to hold the widgets
        label = tk.Label(self, text="Input Base Values")
        label.pack(pady=3, padx=10)

        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        # Create labels and entry boxes for the numbers
        self.label1 = tk.Label(self.frame, text="Enter Baseline Heart Rate:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(self.frame, text="Enter Current Noise Level:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # Button to display the entered values
        submit_button = tk.Button(self.frame, text="Submit", command=self.pass_values)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def start_sim(self):
        self.pass_values()
        self.controller.show_page("HeartbeatSimulation")
    
    def pass_values(self):
        try:
            # Get the values from the entry boxes
            value1 = float(self.entry1.get())
            value2 = float(self.entry2.get())
            self.controller.pages["HeartbeatSimulation"].set_initial_values(value1, value2)
            # Show the values in a messagebox (or you can use other operations)
        except ValueError:
            # Handle case where input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter valid numbers")

class HeartbeatSimulation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initial hr and noise values
        self.baselineHR = 0
        self.hr = 25  # default value
        self.noise = 25  # default value
        self.stress = self.hr + self.noise

        # Modes for HR and Noise
        self.hr_mode = 'normal'    # 'normal' or 'stressed'
        self.noise_mode = 'normal' # 'normal' or 'stressed'

        self.stress_cycles = 0
        self.stress_hr_cycles = 0
        self.stress_noise_cycles = 0

        # Initialize a StringVar for the large display
        self.notif_display = tk.StringVar()
        self.notif_display.set("No notification sent to user")

        # Create a large Label at the top of the window
        large_display_label = tk.Label(self, textvariable=self.notif_display, font=("Helvetica", 16), bg="light grey")
        large_display_label.pack(pady=10)

        # Canvas setup
        self.canvas_width = 1000
        self.canvas_height = 500
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Line segments for the three types of lines
        self.line_segments_hr = []  # Heart rate line
        self.line_segments_noise = []  # Noise line
        self.line_segments_stress = []  # Stress line
        self.x_position = 0
        self.step = 5  # Step size for each segment

        # Initialize StringVars for monitoring
        self.hr_var = tk.StringVar()
        self.hr_var.set(f"HR: {self.hr:.2f}")  # Initial value

        self.noise_var = tk.StringVar()
        self.noise_var.set(f"Noise: {self.noise:.2f}")  # Initial value

        self.stress_var = tk.StringVar()
        self.stress_var.set(f"Stress: {self.stress:.2f}")  # Initial value

        # Stats display
        test_display = tk.Frame(self)
        test_display.pack(side=tk.TOP, pady=10)

        # Create the labels with StringVars
        hr_monitor = tk.Label(test_display, textvariable=self.hr_var)
        hr_monitor.pack()

        noise_monitor = tk.Label(test_display, textvariable=self.noise_var)
        noise_monitor.pack()

        stress_monitor = tk.Label(test_display, textvariable=self.stress_var)
        stress_monitor.pack()

        # Back button
        button = tk.Button(self, text="Back to Start Page", command=lambda: controller.show_page("StartPage"))
        button.pack()

        # Frame for the mode buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.BOTTOM, pady=10)

        # Buttons for modes
        btn_normal = tk.Button(btn_frame, text="Normal", command=self.set_mode_normal)
        btn_normal.pack(side=tk.LEFT, padx=5)

        btn_elevated_sound = tk.Button(btn_frame, text="Elevated Sound", command=self.set_mode_elevated_sound)
        btn_elevated_sound.pack(side=tk.LEFT, padx=5)

        btn_elevated_hr = tk.Button(btn_frame, text="Elevated HR", command=self.set_mode_elevated_hr)
        btn_elevated_hr.pack(side=tk.LEFT, padx=5)

        btn_elevated_both = tk.Button(btn_frame, text="Elevated Sound + HR", command=self.set_mode_elevated_both)
        btn_elevated_both.pack(side=tk.LEFT, padx=5)

    def set_mode_normal(self):
        self.hr_mode = 'normal'
        self.noise_mode = 'normal'
        print("Mode set to Normal")

    def set_mode_elevated_sound(self):
        self.hr_mode = 'normal'
        self.noise_mode = 'stressed'
        print("Mode set to Elevated Sound")

    def set_mode_elevated_hr(self):
        self.hr_mode = 'stressed'
        self.noise_mode = 'normal'
        print("Mode set to Elevated HR")

    def set_mode_elevated_both(self):
        self.hr_mode = 'stressed'
        self.noise_mode = 'stressed'
        print("Mode set to Elevated Sound + HR")
    
    def set_stress_cycles(self):
        if self.stress < 30 and self.stress_cycles + self.stress_hr_cycles + self.stress_noise_cycles != 0:
            self.stress_cycles = 0
            self.stress_hr_cycles = 0
            self.stress_noise_cycles = 0
            self.notif_display.set("Notification: None")
        if 30 < self.stress <= 75:
            if self.hr_mode == 'stressed':
                self.stress_hr_cycles += 1
            else:
                self.stress_noise_cycles += 1
        elif self.stress > 75:
            self.stress_cycles += 1
            self.stress_hr_cycles = 0
            self.stress_noise_cycles = 0
        
        if self.stress_cycles == 50:
            self.notif_display.set("Notification: You appear to be stressed. Take a ten-minute break in a quiet place.")
        elif self.stress_hr_cycles == 50:
            self.notif_display.set("Notification: Your heart rate seems high. Consider resting.")
        elif self.stress_noise_cycles == 50:
            self.notif_display.set("Notification: You are in a dangerously loud environment. Consider moving to quieter place.")
         


    def set_initial_values(self, hr, noise, stress=None):
        """Sets the initial hr and noise values and starts the animation."""
        self.baselineHR = hr
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

    def draw_all(self):
        # Update and draw the heartbeat line
        self.update_hr()
        self.draw_line(self.x_position, self.hr_scaled, "red", self.line_segments_hr)

        # Update and draw the noise line
        self.update_noise()
        self.draw_line(self.x_position, self.noise_scaled, "blue", self.line_segments_noise)

        # Set stress cycles
        self.set_stress_cycles()

        # Determine the color of the stress line based on the stress value
        if self.stress < 30:
            stress_color = "green"
        elif 30 <= self.stress < 75:
            stress_color = "yellow"
        else:
            stress_color = "red"

        # Draw the stress line
        self.draw_line(self.x_position, self.stress_scaled, stress_color, self.line_segments_stress)

        # Increment the x position for drawing
        self.x_position += self.step

        # Shift the line if x_position exceeds 3/4 of the canvas width
        if self.x_position >= 3 * self.canvas_width // 4:
            self.shift_line_left(self.line_segments_hr)
            self.shift_line_left(self.line_segments_noise)
            self.shift_line_left(self.line_segments_stress)

        # Schedule the next segment to be drawn
        self.after(200, self.draw_all)

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

    def update_noise(self):
        if self.noise_mode == 'normal':
            self.noise = normal_decibel_variation(self.noise)
        else:
            self.noise = stressed_decibel_variation(self.noise)
        self.noise_scaled = self.scale_noise(self.noise)
        self.noise_var.set(f"Noise: {self.noise:.2f}")
        self.update_stress()  # Call update_stress after updating noise

    def update_hr(self):
        if self.hr_mode == 'normal':
            self.hr = normalHRGenerator(self.hr)
        else:
            self.hr = stressHRGenerator(self.hr)
        self.hr_scaled = self.scale_hr(self.hr)
        self.hr_var.set(f"HR: {self.hr:.2f}")
        self.update_stress()  # Call update_stress after updating heart rate

    def update_stress(self):
        self.stress = overall_stress_level(self.baselineHR, self.hr, self.noise)
        self.stress_scaled = self.scale_stress(self.stress)
        self.stress_var.set(f"Stress: {self.stress:.2f}")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
