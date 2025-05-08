from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64

def get_key(password):
    """Derive a 32-byte AES key from the password using SHA-256."""
    hasher = SHA256.new()
    hasher.update(password.encode('utf-8'))
    return hasher.digest()

def unpad(data):
    """Remove PKCS7 padding."""
    pad_len = data[-1]
    return data[:-pad_len]

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
    encrypted_b64 = input("Enter the Base64 ciphertext: ")
    password = input("Enter the password: ")
    result = decrypt(encrypted_b64, password)
    print(f"\n🔓 Decrypted Plaintext:\n{result}")
