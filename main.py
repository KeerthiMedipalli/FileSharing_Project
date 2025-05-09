from tkinter import filedialog, Tk
import os
from nacl.utils import random as nacl_random

from encryptor import encrypt_file, decrypt_file, generate_shake_hash
from storage import save_to_local, load_from_local
from blockchain import store_file_on_chain, get_file_metadata

def main():
    print("🔐 Secure Decentralized File Sharing\n")

    # GUI to select file
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select a file to upload")
    if not file_path:
        print("❌ No file selected.")
        return

    print(f"📁 Selected File: {file_path}")

    # Read and encrypt
    with open(file_path, "rb") as f:
        data = f.read()

    key = nacl_random(32)  # 256-bit key
    encrypted_data, nonce = encrypt_file(data, key)
    shake_hash = generate_shake_hash(encrypted_data).hex()

    filename = save_to_local(encrypted_data)
    print(f"✅ File encrypted and saved as: storage/{filename}")
    print(f"🔐 SHAKE256 Hash: {shake_hash}")

    # Simulate blockchain
    bc_record = store_file_on_chain(shake_hash, "Bhanu")
    print("🧾 Blockchain Record:", bc_record)

    # Simulate download and verify
    print("\n📥 Downloading and verifying file...")
    retrieved = load_from_local(filename)
    retrieved_hash = generate_shake_hash(retrieved).hex()

    if retrieved_hash == shake_hash:
        print("✅ File integrity verified.")
        decrypted = decrypt_file(retrieved, key)
        with open("decrypted_output.txt", "wb") as f:
            f.write(decrypted)
        print("🔓 Decryption successful. Output: decrypted_output.txt")
    else:
        print("❗ Hash mismatch. File may be tampered.")

if __name__ == "__main__":
    main()
