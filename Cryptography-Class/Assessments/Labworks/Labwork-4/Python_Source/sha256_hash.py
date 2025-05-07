import hashlib

def sha256_hash(text):
    # Encode the text to bytes
    text_bytes = text.encode('utf-8')
    
    # Create SHA-256 hash object and update with bytes
    hash_object = hashlib.sha256()
    hash_object.update(text_bytes)
    
    # Get the hexadecimal digest of the hash
    hash_hex = hash_object.hexdigest()
    return hash_hex

if __name__ == "__main__":
    plaintext = input("Enter the text to hash with SHA-256: ")
    hashed = sha256_hash(plaintext)
    print(f"\n🔑 SHA-256 Hash:\n{hashed}")
