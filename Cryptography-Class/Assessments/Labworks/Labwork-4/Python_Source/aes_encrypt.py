from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64

def get_key(password):
    """Derive a 32-byte AES key from the password using SHA-256."""
    hasher = SHA256.new()
    hasher.update(password.encode('utf-8'))
    return hasher.digest()

def pad(data):
    """Add PKCS7 padding."""
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def encrypt(plaintext, password):
    try:
        key = get_key(password)
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext.encode('utf-8'))
        ciphertext = cipher.encrypt(padded_plaintext)
        encrypted = base64.b64encode(iv + ciphertext).decode('utf-8')
        return encrypted
    except Exception as e:
        return f"❌ Encryption failed: {e}"

if __name__ == "__main__":
    plaintext = input("Enter the plaintext message: ")
    password = input("Enter the password: ")
    result = encrypt(plaintext, password)
    print(f"\n🔐 Encrypted (Base64):\n{result}")