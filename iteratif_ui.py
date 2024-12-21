import tkinter as tk
from tkinter import messagebox

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

def process_input_iterative():
    try:
        arr1 = list(map(int, entry_arr1.get().strip().split()))
        arr2 = list(map(int, entry_arr2.get().strip().split()))
        arr1.sort()
        arr2.sort()

        # Merge using iterative method
        iterative_result = merge_sorted_iterative(arr1, arr2)

        # Display result
        result_iterative.config(text=f"Iterative Result: {iterative_result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers separated by spaces.")

# Create main application window
root = tk.Tk()
root.title("Merge Sorted Arrays - Iterative")

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
process_button = tk.Button(root, text="Merge and Sort (Iterative)", command=process_input_iterative)
process_button.pack()

# Results label
result_iterative = tk.Label(root, text="Iterative Result: ", fg="blue")
result_iterative.pack()

# Run the application
root.mainloop()
