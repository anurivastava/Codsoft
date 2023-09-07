import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg='#E0E0E0') 

heading = tk.Label(root, text="Calculator", font=("Arial", 20))
heading.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(ipadx=10, ipady=10, padx=20, pady=20, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        command=lambda t=text: button_click(t)
    )
    button.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=10)

clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 16),
    command=clear
)
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

eval_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 16),
    command=evaluate
)
eval_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()
