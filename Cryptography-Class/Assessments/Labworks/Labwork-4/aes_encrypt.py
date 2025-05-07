from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64
import os

def get_key(password):
    """Derive a 32-byte AES key from the password using SHA-256."""
    hasher = SHA256.new()
    hasher.update(password.encode('utf-8'))
    return hasher.digest()

def pad(data):
    """Pad the data using PKCS7 to be multiple of 16 bytes."""
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    """Remove PKCS7 padding."""
    pad_len = data[-1]
    return data[:-pad_len]

def encrypt(plaintext, password):
    key = get_key(password)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode('utf-8'))
    ciphertext = cipher.encrypt(padded)
    encrypted = base64.b64encode(iv + ciphertext).decode('utf-8')
    return encrypted

def decrypt(encrypted_b64, password):
    try:
        key = get_key(password)
        encrypted = base64.b64decode(encrypted_b64)
        iv = encrypted[:16]
        ciphertext = encrypted[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext).decode('utf-8')
        return plaintext
    except Exception as e:
        return f"❌ Decryption failed: {e}"

if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    if choice in ['e', 'encrypt']:
        plaintext = input("Enter the plaintext: ")
        password = input("Enter the password: ")
        encrypted = encrypt(plaintext, password)
        print(f"\n🔐 Encrypted (Base64):\n{encrypted}")
    elif choice in ['d', 'decrypt']:
        encrypted_b64 = input("Enter the Base64 ciphertext: ")
        password = input("Enter the password: ")
        decrypted = decrypt(encrypted_b64, password)
        print(f"\n🔓 Decrypted Plaintext:\n{decrypted}")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
