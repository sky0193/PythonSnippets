import tkinter as tk
from tkinter import ttk
import keyboard

class CountdownApp:
    def __init__(self, master):
        self.master = master

        self.master.overrideredirect(True)

        self.master.title("Countdown Timer")

        # Set the background transparency to 70%
        #self.master.attributes("-alpha", 0.7)

        self.master.geometry("100x100+100+100")
        self.master.wm_attributes("-topmost", 1)
        #self.master.wm_attributes('-transparentcolor','black')
        
        self.count = 15
        self.running = False  # Flag to check if countdown is running

        # Use the keyboard library to set a global hotkey for the F1 key
        keyboard.add_hotkey('F1', self.reset_count)
        keyboard.add_hotkey('F2', self.reset_count)
        keyboard.add_hotkey('F3', self.reset_count)
        keyboard.add_hotkey('F4', self.reset_count)
        keyboard.add_hotkey('F5', self.reset_count)
        keyboard.add_hotkey('F12', self.exit_program)

        self.master.bind('<ButtonPress-1>', self.start_drag)
        self.master.bind('<B1-Motion>', self.drag_window)

        # Create a label widget with transparent background
        self.label = tk.Label(self.master, text="", font=("Helvetica Bold", 32), bg='black', fg='white', anchor='center')
        self.label.pack(fill=tk.BOTH, expand=1)

        self.update_label()  # Call the update_label method to display the countdown text

    def reset_count(self):
        self.count = 14
        if not self.running:
            self.start_countdown()

    def start_countdown(self):
        self.running = True
        if self.count >= 0:
            self.update_label()  # Call update_label to update the countdown text
            self.count -= 1
            self.master.after(1000, self.start_countdown)  # after 1 second (1000 ms), call the function again
        else:
            self.running = False

    def exit_program(self):
        """Exit the program when called."""
        self.master.destroy()

    def start_drag(self, event):
        """Function to get the initial mouse position when starting to drag the window."""
        self.startX = event.x
        self.startY = event.y

    def drag_window(self, event):
        """Function to move the window as the mouse is dragged."""
        x = self.master.winfo_x() + event.x - self.startX
        y = self.master.winfo_y() + event.y - self.startY
        self.master.geometry("+%s+%s" % (x, y))

    def update_label(self):
        """Update the countdown label text."""
        self.label.config(text=str(self.count))


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    app = CountdownApp(root)
    root.mainloop()
