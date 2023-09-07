import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Item", "Please enter an item.")

def remove_item():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("No Item Selected", "Please select an item.")
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x400")
window.configure(bg="#FDFEFE")

bg_frame = tk.Frame(window, bg="#F7DC6F")
bg_frame.pack(fill=tk.BOTH, expand=True)

heading = tk.Label(bg_frame, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#7F8C8D", fg="#FDFEFE", padx=20, pady=10)
heading.pack(fill=tk.X)

frame = tk.Frame(bg_frame, bg="#FDFEFE")
frame.pack(pady=10)


listbox = tk.Listbox(frame, width=30, height=10, bd=0, font=("Helvetica", 12), bg="#FDFEFE", fg="#2C3E50", highlightthickness=0)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
entry_frame = tk.Frame(bg_frame, bg="#FDFEFE")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Helvetica", 12))
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(entry_frame, text="Add Item", font=("Helvetica", 12), bg="#2ECC71", fg="#FDFEFE", command=add_item)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(entry_frame, text="Remove Item", font=("Helvetica", 12), bg="#E74C3C", fg="#FDFEFE", command=remove_item)
remove_button.pack(side=tk.LEFT)

window.mainloop()
