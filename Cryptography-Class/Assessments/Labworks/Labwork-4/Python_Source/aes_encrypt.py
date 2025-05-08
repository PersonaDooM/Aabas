from Crypto.Cipher import AES   #Crypto.Cipher.AES: For AES encryption.
from Crypto.Hash import SHA256  #Crypto.Hash.SHA256: To hash the password into a 256-bit key.
from Crypto.Random import get_random_bytes  #Crypto.Random.get_random_bytes: To generate a random Initialization Vector (IV).
import base64 #base64: To encode the encrypted data into a Base64 string.

def get_key(password):
    """Derive a 32-byte AES key from the password using SHA-256."""
    hasher = SHA256.new()
    hasher.update(password.encode('utf-8'))
    return hasher.digest()
#Converts the password to bytes.
#Hashes it using SHA-256 to produce a 32-byte key, suitable for AES-256.

def pad(data):
    """Add PKCS7 padding."""
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)
#AES requires data length to be a multiple of 16 bytes.
#Implements PKCS#7 padding by appending the number of padding bytes as bytes.

def encrypt(plaintext, password):
    try:
        key = get_key(password)
        iv = get_random_bytes(16)
        automate = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext.encode('utf-8'))
        ciphertext = automate.encrypt(padded_plaintext)
        encrypted = base64.b64encode(iv + ciphertext).decode('utf-8')
        return encrypted
    except Exception as e:
        return f"❌ Encryption failed: {e}"
#Key derivation using the password.
#IV generation for CBC mode.
#Cipher creation with the key and IV.
#Pads and encrypts the plaintext.
#Concatenates IV + ciphertext, encodes with Base64.
#Returns the Base64 string for easy sharing or storing.

if _name_ == "_main_":
    plaintext = input("Enter the plaintext message: ")
    password = input("Enter the password: ")
    result = encrypt(plaintext, password)
    print(f"\n🔐 Encrypted (Base64):\n{result}")