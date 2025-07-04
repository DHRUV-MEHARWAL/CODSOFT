import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# Password generation function
def generate_password():
    length = length_var.get()

    if length < 4:
        messagebox.showerror("Error", "Length must be at least 4")
        return

    chars = ''
    if lowercase_var.get():
        chars += string.ascii_lowercase
    if uppercase_var.get():
        chars += string.ascii_uppercase
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Choose Characters", "Please select at least one character set!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

# Copy password to clipboard
def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("🔐 Fancy Password Generator")
root.geometry("500x450")
root.config(bg="#1e1e2e")

tk.Label(root, text="🔒 Password Generator", font=("Courier", 20, "bold"),
         bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

# Frame for options
options_frame = tk.Frame(root, bg="#1e1e2e")
options_frame.pack(pady=10)

length_var = tk.IntVar(value=12)
tk.Label(options_frame, text="Length:", font=("Arial", 13), bg="#1e1e2e", fg="#cdd6f4").grid(row=0, column=0, padx=5)
tk.Entry(options_frame, textvariable=length_var, width=5, font=("Arial", 13)).grid(row=0, column=1, padx=10)

# Checkboxes
lowercase_var = tk.IntVar(value=1)
uppercase_var = tk.IntVar(value=1)
digits_var = tk.IntVar(value=1)
symbols_var = tk.IntVar(value=1)

tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var,
               bg="#1e1e2e", fg="#a6e3a1", font=("Arial", 12),
               activebackground="#1e1e2e", selectcolor="#1e1e2e").pack(anchor='w', padx=40)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var,
               bg="#1e1e2e", fg="#89dceb", font=("Arial", 12),
               activebackground="#1e1e2e", selectcolor="#1e1e2e").pack(anchor='w', padx=40)

tk.Checkbutton(root, text="Include Numbers (0-9)", variable=digits_var,
               bg="#1e1e2e", fg="#fab387", font=("Arial", 12),
               activebackground="#1e1e2e", selectcolor="#1e1e2e").pack(anchor='w', padx=40)

tk.Checkbutton(root, text="Include Symbols (!@#)", variable=symbols_var,
               bg="#1e1e2e", fg="#f38ba8", font=("Arial", 12),
               activebackground="#1e1e2e", selectcolor="#1e1e2e").pack(anchor='w', padx=40)

# Generate Button
tk.Button(root, text="🎲 Generate Password", command=generate_password,
          bg="#f38ba8", fg="white", font=("Arial", 13), width=22).pack(pady=15)

# Display password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Courier", 16, "bold"), width=30,
         justify='center', state='readonly', bg="#313244", fg="#000000", disabledforeground="#a6e3a1").pack(pady=5)


# Copy button
tk.Button(root, text="📋 Copy to Clipboard", command=copy_password,
          bg="#a6e3a1", fg="black", font=("Arial", 12), width=20).pack(pady=10)

root.mainloop()
