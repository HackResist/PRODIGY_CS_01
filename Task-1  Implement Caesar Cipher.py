#This code written by Lokesh(HackResist)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def encrypt_text():
    plaintext = text_input.get("1.0", tk.END).strip()
    if not plaintext:
        show_message("Please enter a message to encrypt.")
        return

    shift_str = shift_entry.get()
    if not shift_str.isdigit():
        show_message("Shift value must be a positive integer.")
        return

    shift = int(shift_str)
    if shift < 1 or shift > 25:
        show_message("Shift value must be between 1 and 25.")
        return

    encrypted_message = caesar_cipher_encrypt(plaintext, shift)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", encrypted_message)
    text_output.config(state=tk.DISABLED)

def decrypt_text():
    ciphertext = text_input.get("1.0", tk.END).strip()
    if not ciphertext:
        show_message("Please enter a message to decrypt.")
        return

    shift_str = shift_entry.get()
    if not shift_str.isdigit():
        show_message("Shift value must be a positive integer.")
        return

    shift = int(shift_str)
    if shift < 1 or shift > 25:
        show_message("Shift value must be between 1 and 25.")
        return

    decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", decrypted_message)
    text_output.config(state=tk.DISABLED)

def show_message(message):
    messagebox.showinfo("Caesar Cipher Error", message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Set minimum and maximum window size
root.minsize(400, 300)
root.maxsize(800, 600)

# Set solid light color background
root.configure(bg="#6d716f")

# Create a style for the background frames
style = ttk.Style()
style.configure("TFrame", background="#6d716f")
style.configure("Custom.TButton", font=("Arial", 12), foreground="black", background="#52de22")
style.map("Custom.TButton",
          foreground=[('active', '#52de22')],
          background=[('active', '#66a3ff')])

# Function to handle button hover
def on_hover(event):
    event.widget.config(cursor="hand2", relief=tk.RAISED)

# Function to handle button leave
def on_leave(event):
    event.widget.config(cursor="", relief=tk.FLAT)

# Create input frame
input_frame = ttk.Frame(root, padding="10", style="TFrame")
input_frame.pack(fill=tk.BOTH, expand=True)

# Text input
text_input_label = ttk.Label(input_frame, text="Enter Text:", background="#f0f8ff")
text_input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
text_input = tk.Text(input_frame, height=5, wrap=tk.WORD)
text_input.grid(row=0, column=1, padx=5, pady=5)

# Shift value input
shift_label = ttk.Label(input_frame, text="Shift Value (1-25):", background="#f0f8ff")
shift_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
shift_entry = ttk.Entry(input_frame, width=10)
shift_entry.grid(row=1, column=1, padx=5, pady=5)
shift_entry.insert(tk.END, "3")  # Default shift value

# Encryption and Decryption buttons
encrypt_button = ttk.Button(input_frame, text="Encrypt", command=encrypt_text, style="Custom.TButton")
encrypt_button.grid(row=2, column=0, padx=5, pady=10)
encrypt_button.bind("<Enter>", on_hover)
encrypt_button.bind("<Leave>", on_leave)

decrypt_button = ttk.Button(input_frame, text="Decrypt", command=decrypt_text, style="Custom.TButton")
decrypt_button.grid(row=2, column=1, padx=5, pady=10)
decrypt_button.bind("<Enter>", on_hover)
decrypt_button.bind("<Leave>", on_leave)

# Output frame
output_frame = ttk.Frame(root, padding="10", style="TFrame")
output_frame.pack(fill=tk.BOTH, expand=True)

# Output text
text_output_label = ttk.Label(output_frame, text="Result:", background="#f0f8ff")
text_output_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
text_output = tk.Text(output_frame, height=5, wrap=tk.WORD, state=tk.DISABLED)
text_output.grid(row=1, column=0, padx=5, pady=5, sticky="we")

# Configure message box style
style.configure("MessageBox.TFrame", borderwidth=12, relief=tk.RAISED, background="#8b948f", bordercolor="#666666")
style.configure("MessageBox.TLabel", font=("Arial", 12))

root.mainloop()
