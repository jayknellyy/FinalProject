import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Task class to represent each task
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description} - {self.priority}"

class ToDoMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDoMaster")
        self.root.geometry("600x500")
        
        # Task list initialization
        self.tasks = []
        
        # Images (can be used for icons and background)
        self.task_icon = tk.PhotoImage(file="task_icon.png")  # Replace with actual file path
        self.bg_image = tk.PhotoImage(file="background_image.png")  # Replace with actual file path
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        # Title Label
        self.title_label = tk.Label(self.root, text="ToDoMaster", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_label.pack(pady=20)

        # Task List Label
        self.task_list_label = tk.Label(self.root, text="Task List", font=("Helvetica", 14), bg="lightblue")
        self.task_list_label.pack()

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        
        # Message
        self.message_label = tk.Label(self.root, text="Please select a task to edit or delete.", font=("Helvetica", 10), bg="lightblue")
        self.message_label.pack(pady=5)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.root, bg="lightblue")
        self.buttons_frame.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.buttons_frame, text="Add Task", command=self.open_add_task_window)
        self.add_button.grid(row=0, column=0, padx=10)

        # Edit Task Button
        self.edit_button = tk.Button(self.buttons_frame, text="Edit Task", command=self.open_edit_task_window)
        self.edit_button.grid(row=0, column=1, padx=10)

        # Delete Task Button
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=10)

        # Exit Button
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=0, column=3, padx=10)

    def open_add_task_window(self):
        AddTaskWindow(self.root, self)

    def open_edit_task_window(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            EditTaskWindow(self.root, self, task, selected_task_index[0])

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks.remove(task)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def exit_app(self):
        self.root.quit()

    def add_task(self, task):
        self.tasks.append(task)
        self.update_task_listbox()

    def edit_task(self, task, index):
        self.tasks[index] = task
        self.update_task_listbox()

class AddTaskWindow:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.window = tk.Toplevel(parent)
        self.window.title("Add Task")
        self.window.geometry("400x300")

        # Labels
        self.label = tk.Label(self.window, text="Enter Task Details", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.description_label = tk.Label(self.window, text="Task Description")
        self.description_label.pack(pady=5)

        # Task Description Entry
        self.description_entry = tk.Entry(self.window, width=30)
        self.description_entry.pack(pady=5)

        self.priority_label = tk.Label(self.window, text="Priority")
        self.priority_label.pack(pady=5)

        # Task Priority Dropdown
        self.priority_var = tk.StringVar()
        self.priority_dropdown = ttk.Combobox(self.window, textvariable=self.priority_var, values=["High", "Medium", "Low"], state="readonly")
        self.priority_dropdown.set("Medium")
        self.priority_dropdown.pack(pady=5)

        # Buttons
        self.save_button = tk.Button(self.window, text="Save Task", command=self.save_task)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.cancel_button = tk.Button(self.window, text="Cancel", command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=10, pady=10)

    def save_task(self):
        description = self.description_entry.get()
        priority = self.priority_var.get()

        if not description or not priority:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        task = Task(description, priority)
        self.app.add_task(task)
        self.window.destroy()

    def cancel(self):
        self.window.destroy()

class EditTaskWindow:
    def __init__(self, parent, app, task, index):
        self.parent = parent
        self.app = app
        self.task = task
        self.index = index
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Task")
        self.window.geometry("400x300")

        # Labels
        self.label = tk.Label(self.window, text="Edit Task", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.description_label = tk.Label(self.window, text="Edit Task Description")
        self.description_label.pack(pady=5)

        # Task Description Entry
        self.description_entry = tk.Entry(self.window, width=30)
        self.description_entry.insert(0, self.task.description)
        self.description_entry.pack(pady=5)

        self.priority_label = tk.Label(self.window, text="Edit Task Priority")
        self.priority_label.pack(pady=5)

        # Task Priority Dropdown
        self.priority_var = tk.StringVar()
        self.priority_dropdown = ttk.Combobox(self.window, textvariable=self.priority_var, values=["High", "Medium", "Low"], state="readonly")
        self.priority_dropdown.set(self.task.priority)
        self.priority_dropdown.pack(pady=5)

        # Buttons
        self.save_button = tk.Button(self.window, text="Save Task", command=self.save_task)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.cancel_button = tk.Button(self.window, text="Cancel", command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=10, pady=10)

    def save_task(self):
        description = self.description_entry.get()
        priority = self.priority_var.get()

        if not description or not priority:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        task = Task(description, priority)
        self.app.edit_task(task, self.index)
        self.window.destroy()

    def cancel(self):
        self.window.destroy()

# Create the main window and app instance
root = tk.Tk()
app = ToDoMasterApp(root)

# Run the application
root.mainloop()
