import tkinter as tk
import random
import string

def generate_password(length, strength):
    if strength == 'Easy':
        characters = string.ascii_letters + string.digits
    elif strength == 'Medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_update_label():
    password_strength = strength_var.get()
    password_length = int(length_entry.get())
    password = generate_password(password_length, password_strength)
    password_label.config(text=password)

def clear_password_label():
    password_label.config(text='')

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="#3498db")

# Create labels
strength_label = tk.Label(window, text="Select Password Strength:", bg="#3498db", font=("Arial", 12))
strength_label.pack(pady=10)

# Create a dropdown for password strength
strength_var = tk.StringVar()
strength_var.set("Easy")
strength_options = ["Easy", "Medium", "Strong"]
strength_dropdown = tk.OptionMenu(window, strength_var, *strength_options)
strength_dropdown.pack()

# Create a label and entry for password length
length_label = tk.Label(window, text="Enter Password Length:", bg="#3498db", font=("Arial", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack()

# Create a button to generate a password
generate_button = tk.Button(window, text="Generate Password", command=generate_password_and_update_label, bg="#2ecc71", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

# Create a label to display the generated password
password_label = tk.Label(window, text="", bg="#3498db", font=("Arial", 14), wraplength=300)
password_label.pack()

# Create a button to clear the password label
clear_button = tk.Button(window, text="Clear", command=clear_password_label, bg="#e74c3c", fg="white", font=("Arial", 12))
clear_button.pack(pady=10)

window.mainloop()
