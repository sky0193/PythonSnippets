
import tkinter as tk
from tkinter import ttk
import keyboard

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        # Set the background transparency to 70%
        self.master.attributes("-alpha", 1)
        self.master.configure(bg='white')  # Setting background color to white for better visibility
        self.master.geometry("40x80")
        self.master.wm_attributes("-topmost", 1)
        
        self.label = ttk.Label(self.master, text="", font=("Arial", 20), background='white')
        self.label.pack(pady=20)

        self.count = 10
        self.running = False  # Flag to check if countdown is running

        # Use the keyboard library to set a global hotkey for the F1 key
        keyboard.add_hotkey('F1', self.reset_count)

    def reset_count(self):
        self.count = 10
        if not self.running:
            self.start_countdown()

    def start_countdown(self):
        self.running = True
        if self.count >= 0:
            self.label.config(text=str(self.count))
            self.count -= 1
            self.master.after(1000, self.start_countdown)  # after 1 second (1000 ms), call the function again
        else:
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()