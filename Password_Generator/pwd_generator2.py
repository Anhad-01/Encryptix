import random
import sys
import tkinter as tk
from tkinter import messagebox

def generate_passwords():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input for length")
        return
    
    upper = upper_var.get()
    lower = lower_var.get()
    nums = nums_var.get()
    syms = sysms_var.get()
    
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = uppercase.lower()
    digits = "0123456789"
    symbols = "!@#$^&*(){};"

    all_characters = ""

    if upper:
        all_characters += uppercase
    if lower:
        all_characters += lowercase
    if nums: 
        all_characters += digits
    if syms:
        all_characters += symbols
        
    if not all_characters:
        messagebox.showerror("Invalid input", "No character types selected for password generation.")
    amount = 5
    
    passwords = []

    for x in range(amount):
        password = "".join(random.sample(all_characters, length))
        passwords.append(password)
        
    #clearing the listbox
    password_listbox.delete(0, tk.END)
    
    #Inserting new passwords into the listbox
    for password in passwords:
        password_listbox.insert(tk.END, password)
        
def copy_password():
    selected_password = password_listbox.get(tk.ACTIVE)
    if selected_password:
        root.clipboard_clear()
        root.clipboard_append(selected_password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("No selection", "No password selected") 
    
def on_enter(e):
    e.widget['background'] = 'lightblue'
    
def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
    
        
# Setting up the GUI
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text = "Enter the desired length of the password: ").grid(row = 0, column = 0, padx = 0, pady = 0)
length_entry = tk.Entry(root)
length_entry.grid(row = 0, column = 1, padx = 10, pady = 5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
nums_var = tk.BooleanVar()
sysms_var = tk.BooleanVar()

#Buttons for selecting the characters required
tk.Checkbutton(root, text = "Uppercase letters", variable = upper_var).grid(row = 1, column = 0,  padx = 10, pady = 5, sticky = "w")
tk.Checkbutton(root, text = "Lowercase letters", variable = lower_var).grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "w")
tk.Checkbutton(root, text = "Digits", variable = nums_var).grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "w")
tk.Checkbutton(root, text = "Symbols", variable = sysms_var).grid(row = 4, column = 0, padx = 10, pady = 5, sticky = "w")

generate_button = tk.Button(root, text = "Generate passwords", command = generate_passwords, fg = "blue")
generate_button.grid(row = 5, column = 0, columnspan = 2, pady = 10)

#Listbox to show the generate passwords
password_listbox = tk.Listbox(root, width = 50, height = 5)
password_listbox.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 5)

#Copy button
copy_button = tk.Button(root, text = "Copy selected password", command = copy_password, fg = "blue")
copy_button.grid(row = 7, column = 0, columnspan = 2, pady = 10)

#Changing the buttons on hover
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

root.mainloop()
