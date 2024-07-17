import tkinter as tk

root = tk.Tk()
root.geometry('200x50+100+100')  # Change dimensions and position as needed

# Make the window borderless
root.overrideredirect(True)

# Set the window to full transparency
root.attributes('-alpha', 0.1)  

# Create label with desired text color
label = tk.Label(root, text="Your Text Here", font=("Arial", 16), bg='black', fg='white')
label.pack(pady=10, padx=10)

root.mainloop()
