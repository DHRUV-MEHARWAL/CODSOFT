import tkinter as tk
from tkinter import messagebox

# Perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif op == '^':
            result = num1 ** num2
        else:
            result = "Invalid operator"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")

# GUI Setup
window = tk.Tk()
window.title("Calculator")
window.geometry("400x350")
window.config(bg="#1e1e2e")

title = tk.Label(window, text="🧮 Calculator", font=("Courier", 20, "bold"), fg="#f5c2e7", bg="#1e1e2e")
title.pack(pady=10)

entry1 = tk.Entry(window, font=("Arial", 14), justify="center")
entry1.pack(pady=5)

entry2 = tk.Entry(window, font=("Arial", 14), justify="center")
entry2.pack(pady=5)

operator = tk.StringVar()
operator.set('+')

operators_frame = tk.Frame(window, bg="#1e1e2e")
operators_frame.pack(pady=10)

for op in ['+', '-', '*', '/', '^']:
    tk.Radiobutton(operators_frame, text=op, variable=operator, value=op,
                   font=("Arial", 12), fg="#89dceb", bg="#1e1e2e",
                   selectcolor="#313244").pack(side="left", padx=10)

calculate_btn = tk.Button(window, text="Calculate", command=calculate,
                          font=("Arial", 14), bg="#f38ba8", fg="white", relief="ridge")
calculate_btn.pack(pady=15)

result_label = tk.Label(window, text="Result: ", font=("Arial", 14), fg="#a6e3a1", bg="#1e1e2e")
result_label.pack()

window.mainloop()
