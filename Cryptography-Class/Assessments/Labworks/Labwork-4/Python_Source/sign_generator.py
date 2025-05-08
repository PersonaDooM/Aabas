from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

def create_signature(message, private_key_b64):
    try:
        # Decode Base64 private key
        private_key_bytes = base64.b64decode(private_key_b64)
        private_key = RSA.import_key(private_key_bytes)

        # Hash the message
        has
        h = SHA256.new(message.encode('utf-8'))

        # Create signature using PKCS#1 v1.5
        signature = pkcs1_15.new(private_key).sign(hash)

        # Return signature as Base64
        return base64.b64encode(signature).decode('utf-8')
    except Exception as e:
        return f"❌ Error creating signature: {e}"

if __name__ == "__main__":
    message = input("Enter the message to sign: ")
    private_key_b64 = input("\nEnter the RSA private key (Base64): ")

    signature_b64 = create_signature(message, private_key_b64)
    print(f"\n✍️ Digital Signature (Base64):\n{signature_b64}")
