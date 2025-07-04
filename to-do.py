import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASK_FILE = "tasks.txt"

# Load tasks with checkbox state
def load_tasks():
    task_list = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                if line.strip():
                    checked, text = line.strip().split("||", 1)
                    var = tk.IntVar(value=int(checked))
                    task_list.append((var, text))
    return task_list

# Save tasks with checkbox state
def save_tasks():
    with open(TASK_FILE, "w") as file:
        for var, task in tasks:
            file.write(f"{var.get()}||{task}\n")

# Add a task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter a new task:")
    if task:
        var = tk.IntVar()
        tasks.append((var, task))
        update_task_list()
        save_tasks()

# Clear all tasks
def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        for widget in task_frame.winfo_children():
            widget.destroy()
        tasks.clear()
        save_tasks()

# Update the display list
def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for var, task in tasks:
        cb = tk.Checkbutton(task_frame, text=task, variable=var,
                            font=("Arial", 13),
                            bg="#1e1e2e", fg="#cdd6f4",
                            activebackground="#1e1e2e",
                            selectcolor="#1e1e2e",
                            command=save_tasks)
        cb.pack(anchor="w", pady=2)

# GUI setup
root = tk.Tk()
root.title("🗒️ Fancy To-Do List")
root.geometry("500x500")
root.config(bg="#1e1e2e")

tk.Label(root, text="🌟 Your To-Do List", font=("Courier", 18, "bold"),
         bg="#1e1e2e", fg="#f5c2e7").pack(pady=10)

# Scrollable Frame for tasks
task_canvas = tk.Canvas(root, bg="#1e1e2e", highlightthickness=0)
task_canvas.pack(side="left", fill="both", expand=True, padx=(20,0))

scrollbar = tk.Scrollbar(root, orient="vertical", command=task_canvas.yview)
scrollbar.pack(side="right", fill="y")

task_frame = tk.Frame(task_canvas, bg="#1e1e2e")
task_frame.bind("<Configure>", lambda e: task_canvas.configure(scrollregion=task_canvas.bbox("all")))
task_canvas.create_window((0, 0), window=task_frame, anchor="nw")
task_canvas.configure(yscrollcommand=scrollbar.set)

# Button Frame
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.place(relx=0.5, rely=0.92, anchor="s")

tk.Button(button_frame, text="➕ Add Task", command=add_task,
          bg="#a6e3a1", fg="black", width=12).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="🧹 Clear All", command=clear_all,
          bg="#f38ba8", fg="black", width=12).grid(row=0, column=1, padx=10)

# Load and display tasks
tasks = load_tasks()
update_task_list()

root.mainloop()
