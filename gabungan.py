import tkinter as tk
from tkinter import messagebox
import time

def merge_sorted_iterative(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

def merge_sorted_recursive(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge_sorted_recursive(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge_sorted_recursive(arr1, arr2[1:])

def process_input():
    try:
        arr1 = list(map(int, entry_arr1.get().strip().split()))
        arr2 = list(map(int, entry_arr2.get().strip().split()))
        arr1.sort()
        arr2.sort()

        # Measure time for iterative method
        start_time = time.time()
        iterative_result = merge_sorted_iterative(arr1, arr2)
        iterative_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Measure time for recursive method
        start_time = time.time()
        recursive_result = merge_sorted_recursive(arr1, arr2)
        recursive_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Display results
        result_iterative.config(
            text=f"Iterative: {iterative_result} (Time: {iterative_time:.2f} ms)"
        )
        result_recursive.config(
            text=f"Recursive: {recursive_result} (Time: {recursive_time:.2f} ms)"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers separated by spaces.")

# Create main application window
root = tk.Tk()
root.title("Merge Sorted Arrays")

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
process_button = tk.Button(root, text="Merge and Sort", command=process_input)
process_button.pack()

# Results labels
result_iterative = tk.Label(root, text="Iterative: ", fg="blue")
result_iterative.pack()

result_recursive = tk.Label(root, text="Recursive: ", fg="green")
result_recursive.pack()

# Run the application
root.mainloop()
