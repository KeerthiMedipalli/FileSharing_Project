import os
import hashlib

def save_to_local(encrypted_data: bytes):
    filename = hashlib.sha256(encrypted_data).hexdigest()[:10] + ".bin"
    os.makedirs("storage", exist_ok=True)
    path = os.path.join("storage", filename)
    with open(path, "wb") as f:
        f.write(encrypted_data)
    return filename

def load_from_local(filename):
    path = os.path.join("storage", filename)
    with open(path, "rb") as f:
        return f.read()
