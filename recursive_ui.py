import tkinter as tk
from tkinter import messagebox

def merge_sorted_recursive(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge_sorted_recursive(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge_sorted_recursive(arr1, arr2[1:])

def process_input_recursive():
    try:
        arr1 = list(map(int, entry_arr1.get().strip().split()))
        arr2 = list(map(int, entry_arr2.get().strip().split()))
        arr1.sort()
        arr2.sort()

        # Merge using recursive method
        recursive_result = merge_sorted_recursive(arr1, arr2)

        # Display result
        result_recursive.config(text=f"Recursive Result: {recursive_result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers separated by spaces.")

# Create main application window
root = tk.Tk()
root.title("Merge Sorted Arrays - Recursive")

# Input labels and entries
label_arr1 = tk.Label(root, text="Enter Array 1 (space-separated):")
label_arr1.pack()
entry_arr1 = tk.Entry(root, width=50)
entry_arr1.pack()

label_arr2 = tk.Label(root, text="Enter Array 2 (space-separated):")
label_arr2.pack()
entry_arr2 = tk.Entry(root, width=50)
entry_arr2.pack()

# Process button
process_button = tk.Button(root, text="Merge and Sort (Recursive)", command=process_input_recursive)
process_button.pack()

# Results label
result_recursive = tk.Label(root, text="Recursive Result: ", fg="green")
result_recursive.pack()

# Run the application
root.mainloop()
