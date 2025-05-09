import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class FileEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption and Decryption")
        self.root.geometry("500x400")
        self.root.config(bg="#f4f4f9")
        
        self.key = None
        
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Secure File Encryption", font=("Helvetica", 18), bg="#f4f4f9", fg="#4CAF50")
        self.title_label.pack(pady=20)

        self.encrypt_button = tk.Button(self.root, text="Encrypt File", command=self.encrypt_file, bg="#4CAF50", fg="white", font=("Arial", 14), relief="raised", width=20)
        self.encrypt_button.pack(pady=10)
        
        self.decrypt_button = tk.Button(self.root, text="Decrypt File", command=self.decrypt_file, bg="#FF5722", fg="white", font=("Arial", 14), relief="raised", width=20)
        self.decrypt_button.pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="Select a file to encrypt or decrypt", font=("Arial", 12), bg="#f4f4f9")
        self.status_label.pack(pady=20)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="indeterminate")
        self.progress.pack(pady=10)
        
    def encrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select a file to encrypt")
        if file_path:
            self.status_label.config(text=f"Encrypting: {os.path.basename(file_path)}")
            self.progress.start()
            # Simulate encryption here (replace with actual encryption logic)
            encrypted_file = self.simulate_encryption(file_path)
            self.progress.stop()
            messagebox.showinfo("Success", f"File encrypted successfully! Saved at {encrypted_file}")
            self.status_label.config(text="Select a file to encrypt or decrypt")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select a file to decrypt")
        if file_path:
            self.status_label.config(text=f"Decrypting: {os.path.basename(file_path)}")
            self.progress.start()
            # Simulate decryption here (replace with actual decryption logic)
            decrypted_file = self.simulate_decryption(file_path)
            self.progress.stop()
            messagebox.showinfo("Success", f"File decrypted successfully! Saved at {decrypted_file}")
            self.status_label.config(text="Select a file to encrypt or decrypt")

    def simulate_encryption(self, file_path):
        # Simulate encryption here (replace with actual encryption logic)
        encrypted_file_path = file_path + '.enc'
        return encrypted_file_path

    def simulate_decryption(self, file_path):
        # Simulate decryption here (replace with actual decryption logic)
        decrypted_file_path = file_path.replace('.enc', '')
        return decrypted_file_path

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptionApp(root)
    root.mainloop()
