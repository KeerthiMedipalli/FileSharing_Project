import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import hashlib
import json
from time import time

# Simulated encryption and decryption functions (use actual logic in production)
def encrypt_file_data(file_path):
    encrypted_path = file_path + ".enc"
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(encrypted_path, 'wb') as f:
        f.write(data[::-1])  # Just reversing bytes for demo
    return encrypted_path

def decrypt_file_data(file_path):
    decrypted_path = file_path.replace(".enc", "_decrypted")
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(decrypted_path, 'wb') as f:
        f.write(data[::-1])
    return decrypted_path

# Basic Blockchain for action logging
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_logs = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.create_block(previous_hash='0', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'logs': self.current_logs,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.current_logs = []
        self.chain.append(block)
        return block

    def add_log(self, action, filename, result_path):
        log = {
            'action': action,
            'filename': filename,
            'result_path': result_path,
            'timestamp': time()
        }
        self.current_logs.append(log)
        if len(self.current_logs) >= 2:
            self.create_block(proof=100, previous_hash=self.hash(self.chain[-1]))

    def hash(self, block):
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    def get_chain(self):
        return self.chain

blockchain = Blockchain()

# GUI Application
class EncryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Encryptor with Blockchain")
        self.master.geometry("700x550")
        self.master.configure(bg="#eef2f3")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Secure File Encryptor & Blockchain Logger", font=("Helvetica", 16, "bold"), bg="#eef2f3", fg="#2c3e50").pack(pady=20)

        self.status_label = tk.Label(self.master, text="Choose a file to begin", font=("Arial", 12), bg="#eef2f3")
        self.status_label.pack(pady=10)

        tk.Button(self.master, text="Encrypt File", command=self.encrypt_file, bg="#27ae60", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.master, text="Decrypt File", command=self.decrypt_file, bg="#c0392b", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.master, text="Show Blockchain", command=self.show_blockchain, bg="#2980b9", fg="white", font=("Arial", 12), width=20).pack(pady=5)

        self.progress = ttk.Progressbar(self.master, orient="horizontal", length=400, mode="indeterminate")
        self.progress.pack(pady=20)

        self.output_box = tk.Text(self.master, height=10, width=80, wrap=tk.WORD)
        self.output_box.pack(pady=10)
        self.output_box.insert(tk.END, "Logs will be shown here...
")

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.progress.start()
            encrypted = encrypt_file_data(file_path)
            blockchain.add_log("encrypt", os.path.basename(file_path), encrypted)
            self.progress.stop()
            self.status_label.config(text=f"Encrypted file saved at: {encrypted}")
            self.output_box.insert(tk.END, f"Encrypted {file_path} → {encrypted}
")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
        if file_path:
            self.progress.start()
            decrypted = decrypt_file_data(file_path)
            blockchain.add_log("decrypt", os.path.basename(file_path), decrypted)
            self.progress.stop()
            self.status_label.config(text=f"Decrypted file saved at: {decrypted}")
            self.output_box.insert(tk.END, f"Decrypted {file_path} → {decrypted}
")

    def show_blockchain(self):
        chain_window = tk.Toplevel(self.master)
        chain_window.title("Blockchain Viewer")
        chain_window.geometry("700x400")

        text_area = tk.Text(chain_window, wrap=tk.WORD)
        text_area.pack(fill=tk.BOTH, expand=1)
        chain_data = json.dumps(blockchain.get_chain(), indent=4)
        text_area.insert(tk.END, chain_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
