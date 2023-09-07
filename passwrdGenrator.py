import random
import tkinter as tk

def generate_password():
    length = int(length_entry.get())
    if length >= 6:
        characters = '''abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
        password = "".join(random.sample(characters, length))
        password_label.config(text=password)
    else:
        password_label.config(text="Password length must be at least 6")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#E6F3FF")
root.resizable(False, False)

heading_label = tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), bg="#E6F3FF")
heading_label.pack(pady=20)

length_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
length_frame.pack(pady=20)

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12))
length_label.pack(side=tk.LEFT, padx=10)

length_entry = tk.Entry(length_frame, font=("Arial", 12), width=5)
length_entry.pack(side=tk.LEFT)

length_entry.insert(0, "8")

password_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
password_frame.pack(pady=20)

password_label = tk.Label(password_frame, text="", font=("Arial", 16))
password_label.pack(pady=10,fill="x")

generate_button = tk.Button(password_frame, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

root.mainloop()
