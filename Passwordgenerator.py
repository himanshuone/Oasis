import tkinter as tk
import string
import random

# Define password complexity levels
complexity_levels = {
    "Low": (6, True, True, False),
    "Medium": (8, True, True, True),
    "High": (12, True, True, True),
    "Custom": None
}

# Function to generate random password
def generate_password():

    
    level = complexity_select.get()
    if level == "Custom":
        length = int(length_entry.get())
        lowercase_check = tk.Checkbutton(custom_frame, text="Lowercase", variable=tk.IntVar(value=1))
        uppercase_check = tk.Checkbutton(custom_frame, text="Uppercase", variable=tk.IntVar(value=1))
        symbols_check = tk.Checkbutton(custom_frame, text="Symbols", variable=tk.IntVar(value=1))
    else:
        length, lowercase, uppercase, symbols = complexity_levels[level]
    charset = ""
    if lowercase:
        charset += string.ascii_lowercase
    if uppercase:
        charset += string.ascii_uppercase
    if symbols:
        charset += "!@#$%^&*(){}[]:;<>,./?'"
    password = "".join(random.sample(charset, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Advanced Password Generator")

# Define password complexity options frame
complexity_frame = tk.LabelFrame(root, text="Password Complexity")
complexity_frame.pack(pady=10)

complexity_select = tk.StringVar()
complexity_select.set("Medium")
complexity_options = tk.Radiobutton(complexity_frame, text="Low", variable=complexity_select, value="Low")
complexity_options.pack()
complexity_options = tk.Radiobutton(complexity_frame, text="Medium", variable=complexity_select, value="Medium")
complexity_options.pack()
complexity_options = tk.Radiobutton(complexity_frame, text="High", variable=complexity_select, value="High")
complexity_options.pack()
complexity_options = tk.Radiobutton(complexity_frame, text="Custom", variable=complexity_select, value="Custom")
complexity_options.pack()

# Define custom complexity options frame (optional)
custom_frame = tk.Frame(complexity_frame)

# Pack custom frame only when "Custom" is selected
custom_frame.pack(pady=5)

length_label = tk.Label(custom_frame, text="Length:")
length_label.pack(side="left")
length_entry = tk.Entry(custom_frame, width=5)
length_entry.pack(side="left")

lowercase_check = tk.Checkbutton(custom_frame, text="Lowercase")
lowercase_check.pack(side="left")
uppercase_check = tk.Checkbutton(custom_frame, text="Uppercase")
uppercase_check.pack(side="left")
symbols_check = tk.Checkbutton(custom_frame, text="Symbols")
symbols_check.pack(side="left")

# Define password generation button and entry
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Define clipboard copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: root.clipboard_append(password_entry.get()))
copy_button.pack()

# Run the main loop
root.mainloop()
