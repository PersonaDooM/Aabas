from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def decrypt_rsa(ciphertext_b64, private_key_b64):
    try:
        # Decode the Base64 encoded private key and ciphertext
        private_key_bytes = base64.b64decode(private_key_b64)
        ciphertext_bytes = base64.b64decode(ciphertext_b64)
        
        # Import the private key from the decoded bytes
        private_key = RSA.import_key(private_key_bytes)
        
        # Create the cipher object using the private key and OAEP scheme
        cipher = PKCS1_OAEP.new(private_key)
        
        # Decrypt the ciphertext
        plaintext_bytes = cipher.decrypt(ciphertext_bytes)
        
        # Decode the plaintext bytes to string
        plaintext = plaintext_bytes.decode('utf-8')
        
        return plaintext
    except Exception as e:
        return f"❌ Decryption failed: {e}"

if __name__ == "__main__":
    # Input: ciphertext and private key in Base64 format
    ciphertext_b64 = input("Enter the Base64 ciphertext: ")
    private_key_b64 = input("Enter the Base64 private key: ")
    
    # Decrypt and print the result
    decrypted_message = decrypt_rsa(ciphertext_b64, private_key_b64)
    print(f"\n🔓 Decrypted Message:\n{decrypted_message}")
