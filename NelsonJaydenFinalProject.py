"""
Name: Jayden Nelson
Date Written: 12/13/2024
Assignment: Final Project 
Description: This application is a To Do List that allows you to fiter the tasks out by completed, due dates, and priority.
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import datetime
import re  # Import regex for validation

# Function to validate the due date (YYYY-MM-DD format)
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to validate priority (must be one of 'Low', 'Medium', 'High')
def is_valid_priority(priority):
    return priority in ['Low', 'Medium', 'High']

# Function to add a new task to the list with validation
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    labels = labels_entry.get()
    assigned_person = assigned_person_entry.get()

    # Validate input fields
    if task == "":
        messagebox.showerror("Input Error", "Task cannot be empty!")
        return
    
    if not is_valid_priority(priority):
        messagebox.showerror("Input Error", "Priority must be Low, Medium, or High!")
        return
    
    if due_date != "" and not is_valid_date(due_date):
        messagebox.showerror("Input Error", "Due date must be in the format YYYY-MM-DD!")
        return
    
    # Optional: Validate that assigned person is not empty or contains unwanted characters
    if assigned_person and not re.match("^[A-Za-z ]*$", assigned_person):
        messagebox.showerror("Input Error", "Assigned person must only contain letters and spaces!")
        return

    # Add task if all validations pass
    task_listbox.insert(tk.END, f"{task} | Priority: {priority} | Due: {due_date} | Labels: {labels} | Assigned to: {assigned_person}")
    update_task_count()
    clear_task_input()
    show_main_window()

# Callback function 2 for adding a task (updates task count)
def update_task_count():
    task_count = len(task_listbox.get(0, tk.END))
    task_count_label.config(text=f"Total tasks: {task_count}")

# Callback function 3 for adding a task (clears the input fields)
def clear_task_input():
    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    labels_entry.delete(0, tk.END)
    assigned_person_entry.delete(0, tk.END)

# Function to mark a task as completed
def mark_completed():
    try:
        # Get the index of the selected task
        selected_task_index = task_listbox.curselection()
        
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
            return
        
        # Get the task text
        task = task_listbox.get(selected_task_index)
        
        # Add "Completed" to the task and change its appearance (for example, strikethrough)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"{task} (Completed)")
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})
        
        update_completed_task_label(task)
        
    except Exception as e:
        print("Error marking task as completed:", e)

# Callback function 2 for marking a task as completed (updates the completed task label)
def update_completed_task_label(task):
    completed_label.config(text=f"Last task marked as completed: {task}")

# Callback function 3 for marking a task as completed (updates task count again)
def refresh_task_count_after_completion():
    update_task_count()

# Function to confirm and exit the application
def confirm_exit():
    exit_response = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    if exit_response:
        save_changes_before_exit()
        exit_app()

# Callback function 2 for the exit button (saves changes before exiting)
def save_changes_before_exit():
    # Placeholder for saving task data
    print("Saving changes...")

# Callback function 3 for the exit button (exit the application gracefully)
def exit_app():
    main_window.quit()

# Function to show the main window (To-Do List)
def show_main_window():
    add_task_window.withdraw()  # Hide the Add Task window
    filter_window.withdraw()    # Hide the Filter window
    main_window.deiconify()     # Show the main window

# Function to show the filter window
def show_filter_window():
    main_window.withdraw()      # Hide the main window
    add_task_window.withdraw()  # Hide the Add Task window
    filter_window.deiconify()   # Show the Filter window

# Function to show the add task window
def show_add_task_window():
    main_window.withdraw()      # Hide the main window
    filter_window.withdraw()    # Hide the Filter window
    add_task_window.deiconify() # Show the Add Task window

# Function to apply filters to tasks (not implemented yet)
def apply_filters():
    # For now, we just show a message that filters are applied
    messagebox.showinfo("Filters", "Filters applied (This feature is a placeholder).")

# Set up main window
main_window = tk.Tk()
main_window.title("To-Do List Application")

# Set up window size and icon (using image)
main_window.geometry("400x400")
try:
    main_window.iconphoto(False, PhotoImage(file="icon.png"))
except Exception as e:
    print("Icon image not found:", e)

# Set up main window widgets
task_label = tk.Label(main_window, text="To-Do List", font=("Arial", 18))
task_label.pack(pady=10)

# Create a Listbox to show tasks
task_listbox = tk.Listbox(main_window, width=50, height=10)
task_listbox.pack(pady=10)

# Label to show task count
task_count_label = tk.Label(main_window, text="Total tasks: 0", font=("Arial", 12))
task_count_label.pack(pady=5)

# Label for general instructions
instruction_label = tk.Label(main_window, text="Manage your tasks here", font=("Arial", 12))
instruction_label.pack(pady=5)

# Label to show the last completed task
completed_label = tk.Label(main_window, text="Last task marked as completed: None", font=("Arial", 12))
completed_label.pack(pady=5)

# Add buttons to navigate
add_task_button = tk.Button(main_window, text="Add Task", command=show_add_task_window)
add_task_button.pack(pady=5)

mark_completed_button = tk.Button(main_window, text="Mark Completed", command=mark_completed)
mark_completed_button.pack(pady=5)

filter_button = tk.Button(main_window, text="Filter Tasks", command=show_filter_window)
filter_button.pack(pady=5)

exit_button = tk.Button(main_window, text="Exit", command=confirm_exit)
exit_button.pack(pady=5)

# Add Task Window
add_task_window = tk.Toplevel(main_window)
add_task_window.title("Add New Task")

# Set up window size and icon (using image)
add_task_window.geometry("400x300")
try:
    add_task_window.iconphoto(False, PhotoImage(file="icon.png"))
except Exception as e:
    print("Icon image not found:", e)

# Set up widgets for the add task window
task_entry_label = tk.Label(add_task_window, text="Enter Task:", font=("Arial", 12))
task_entry_label.pack(pady=10)

task_entry = tk.Entry(add_task_window, width=40)
task_entry.pack(pady=5)

priority_label = tk.Label(add_task_window, text="Priority (Low, Medium, High):", font=("Arial", 12))
priority_label.pack(pady=5)

priority_var = tk.StringVar()
priority_menu = tk.OptionMenu(add_task_window, priority_var, "Low", "Medium", "High")
priority_menu.pack(pady=5)

due_date_label = tk.Label(add_task_window, text="Due Date (YYYY-MM-DD):", font=("Arial", 12))
due_date_label.pack(pady=5)

due_date_entry = tk.Entry(add_task_window, width=40)
due_date_entry.pack(pady=5)

labels_label = tk.Label(add_task_window, text="Labels (e.g., Work, Personal):", font=("Arial", 12))
labels_label.pack(pady=5)

labels_entry = tk.Entry(add_task_window, width=40)
labels_entry.pack(pady=5)

assigned_person_label = tk.Label(add_task_window, text="Assigned Person:", font=("Arial", 12))
assigned_person_label.pack(pady=5)

assigned_person_entry = tk.Entry(add_task_window, width=40)
assigned_person_entry.pack(pady=5)

add_button = tk.Button(add_task_window, text="Add Task", command=add_task)
add_button.pack(pady=5)

cancel_button = tk.Button(add_task_window, text="Cancel", command=show_main_window)
cancel_button.pack(pady=5)

# Filter Window
filter_window = tk.Toplevel(main_window)
filter_window.title("Filter Tasks")

# Set up window size and icon (using image)
filter_window.geometry("400x400")
try:
    filter_window.iconphoto(False, PhotoImage(file="icon.png"))
except Exception as e:
    print("Icon image not found:", e)

# Set up filter window widgets
priority_filter_label = tk.Label(filter_window, text="Filter by Priority:", font=("Arial", 12))
priority_filter_label.pack(pady=5)

priority_filter_var = tk.StringVar()
priority_filter_menu = tk.OptionMenu(filter_window, priority_filter_var, "Low", "Medium", "High")
priority_filter_menu.pack(pady=5)

status_filter_label = tk.Label(filter_window, text="Filter by Status:", font=("Arial", 12))
status_filter_label.pack(pady=5)

status_filter_var = tk.StringVar()
status_filter_menu = tk.OptionMenu(filter_window, status_filter_var, "Completed", "Incomplete")
status_filter_menu.pack(pady=5)

due_date_filter_label = tk.Label(filter_window, text="Filter by Due Date (YYYY-MM-DD):", font=("Arial", 12))
due_date_filter_label.pack(pady=5)

due_date_filter_entry = tk.Entry(filter_window, width=40)
due_date_filter_entry.pack(pady=5)

apply_filter_button = tk.Button(filter_window, text="Apply Filters", command=apply_filters)
apply_filter_button.pack(pady=5)

cancel_filter_button = tk.Button(filter_window, text="Cancel", command=show_main_window)
cancel_filter_button.pack(pady=5)

# Start by showing the main window
show_main_window()

# Start the Tkinter event loop
main_window.mainloop()
