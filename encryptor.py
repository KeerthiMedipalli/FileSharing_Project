import os
from Crypto.Cipher import ChaCha20
from Crypto.Hash import SHAKE256
from Crypto.Random import get_random_bytes

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    key = get_random_bytes(32)
    nonce = get_random_bytes(12)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(data)

    shake = SHAKE256.new()
    shake.update(ciphertext)
    file_hash = shake.read(32).hex()

    out_filename = f"storage/{file_hash[:10]}.bin"
    with open(out_filename, 'wb') as f:
        f.write(ciphertext)

    return out_filename, file_hash
