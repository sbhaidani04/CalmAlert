import tkinter as tk
from tkinter import messagebox

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
        for Page in (StartPage, CalmAlert):
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

        button1 = tk.Button(self, text="Open Calm Alert app", 
                            command=lambda: controller.show_page("CalmAlert"))
        button1.pack()

        # Create a frame to hold the widgets
        label = tk.Label(self, text="Input Base Values")
        label.pack(pady=3, padx=10)

        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)  # Make sure the frame itself is packed into the root window

        # Create labels and entry boxes for the numbers
        self.label1 = tk.Label(self.frame, text="Enter number 1:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(self.frame, text="Enter number 2:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.selected_color = tk.StringVar()
        self.selected_color.set("Red")  # Default value

        # Create radio buttons
        colors = ["Stressed", "Calm"]
        for i in range(len(colors)):
            radio_button = tk.Radiobutton(self.frame, text=colors[i], variable=self.selected_color, value=colors[i], command=self.pass_state)
            radio_button.grid(row=2,column=i)

        # Button to display the entered values
        submit_button = tk.Button(self.frame, text="Submit", command=self.pass_values)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def pass_values(self):
        try:
            # Get the values from the entry boxes
            value1 = float(self.entry1.get())
            value2 = float(self.entry2.get())
            self.controller.pages["CalmAlert"].set_value(value1,"HEART")
            self.controller.pages["CalmAlert"].set_value(value2,"SOUND")
            # Show the values in a messagebox (or you can use other operations)
            messagebox.showinfo("Values", f"Value 1: {value1}\nValue 2: {value2}")
        except ValueError:
            # Handle case where input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    
    def pass_state(self):
        """Update the result label with the selected color."""
        selected = self.selected_color.get()
        self.controller.pages["CalmAlert"].set_value(selected)


class CalmAlert(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="CalmAlert")
        label.pack(pady=10, padx=10)

        self.state = None

        self.heart_value = None
        self.hearing_value = None

        self.heart_label = tk.Label(self, text="Value from Page 1:")
        self.heart_label.pack(pady=10)

        self.heart_value_label = tk.Label(self, text="")
        self.heart_value_label.pack(pady=10)

        self.hearing_label = tk.Label(self, text="Value from Page 1:")
        self.hearing_label.pack(pady=10)

        self.hearing_value_label = tk.Label(self, text="")
        self.hearing_value_label.pack(pady=10)

        button = tk.Button(self, text="Back to Start Page", 
                           command=lambda: controller.show_page("StartPage"))
        button.pack()

    def set_value(self, value, type):
        if type == "HEART":
            self.heart_value = int(value)
            self.heart_value_label.config(text=value)
        else:
            self.hearing_value = int(value)
            self.hearing_value_label.config(text=value)
        
        print(self.heart_value)
        print(self.hearing_value)

    def set_state(self, value):
        self.state = value

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()