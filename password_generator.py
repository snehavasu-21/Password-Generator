import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # pip install pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Options", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    pyperclip.copy(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Password Length:", font="Arial 12").pack(pady=5)
length_entry = tk.Entry(root, font="Arial 12", justify="center")
length_entry.pack(pady=5)

# Checkbuttons
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

frame = tk.Frame(root)
frame.pack()

tk.Checkbutton(frame, text="Uppercase", variable=var_upper).grid(row=0, column=0)
tk.Checkbutton(frame, text="Lowercase", variable=var_lower).grid(row=0, column=1)
tk.Checkbutton(frame, text="Numbers", variable=var_digits).grid(row=1, column=0)
tk.Checkbutton(frame, text="Symbols", variable=var_symbols).grid(row=1, column=1)

tk.Button(root, text="Generate", font="Arial 12", command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, font="Arial 12", justify="center")
result_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

root.mainloop()
