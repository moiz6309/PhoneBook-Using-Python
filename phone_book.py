import tkinter as tk
from tkinter import messagebox
import os

# File to store the phonebook data
PHONEBOOK_FILE = "phonebook1.txt"
# Function to load phonebook data from file
def load_phonebook():
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, "r") as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line and ":" in line:  # Ensure the line isn't empty and contains a colon
                    name, phone = line.split(":", 1)  # Split at the first colon
                    phonebook[name] = phone
                else:
                    print(f"Skipping invalid line: {line}")  # Log the invalid line for debugging
# Function to save a contact to the file
def save_contact_to_file(name, phone):
    with open(PHONEBOOK_FILE, "a") as file:
        file.write(f"{name}:{phone}\n")

# Function to add a contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Both name and phone number are required.")
        return

    if name in phonebook:
        messagebox.showwarning("Duplicate Entry", f"Contact '{name}' already exists.")
        return

    phonebook[name] = phone
    save_contact_to_file(name, phone)
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to search for a contact (by name or phone number)
def search_contact():
    search_input = search_entry.get().strip()

    if search_input == "":
        messagebox.showwarning("Input Error", "Please enter a name or phone number to search.")
        return

    # Search by name
    if search_input in phonebook:
        name = search_input
        phone = phonebook[name]
        result_label.config(text=f"Name: {name}\nPhone: {phone}")
        return

    # Search by phone number
    for name, phone in phonebook.items():
        if phone == search_input:
            result_label.config(text=f"Name: {name}\nPhone: {phone}")
            return

    # If not found
    result_label.config(text="Contact not found.")

# Initialize the phonebook dictionary
phonebook = {}
load_phonebook()

# Create the main window
root = tk.Tk()
root.title("Phonebook")
root.geometry("400x400")
root.resizable(False, False)

# Add Contact Section
tk.Label(root, text="Add Contact", font=("Arial", 14, "bold")).pack(pady=10)
add_frame = tk.Frame(root)
add_frame.pack(pady=5)

tk.Label(add_frame, text="Name: ").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(add_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(add_frame, text="Phone: ").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(add_frame, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(add_frame, text="Add Contact", command=add_contact, bg="lightblue").grid(row=2, columnspan=2, pady=10)

# Search Contact Section
tk.Label(root, text="Search Contact", font=("Arial", 14, "bold")).pack(pady=10)
search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Label(search_frame, text="Enter Name or Phone: ").grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(search_frame, text="Search", command=search_contact, bg="lightgreen").grid(row=1, columnspan=2, pady=10)

# Result Section
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()