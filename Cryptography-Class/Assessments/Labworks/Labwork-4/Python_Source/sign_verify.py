from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

def verify_signature(message, signature_b64, public_key_b64):
    try:
        # Decode Base64 public key and load it
        public_key_bytes = base64.b64decode(public_key_b64)
        public_key = RSA.import_key(public_key_bytes)

        # Decode the Base64 signature
        signature = base64.b64decode(signature_b64)

        # Hash the message
        h = SHA256.new(message.encode('utf-8'))

        # Verify the signature
        pkcs1_15.new(public_key).verify(h, signature)
        return "✅ Signature is valid."
    except (ValueError, TypeError) as e:
        return f"❌ Signature is invalid: {e}"

if __name__ == "__main__":
    print("Enter the original message:")
    message = input().strip()

    print("\nEnter the digital signature (Base64):")
    signature_b64 = input().strip()

    print("\nEnter the RSA public key (Base64):")
    public_key_b64 = input().strip()

    result = verify_signature(message, signature_b64, public_key_b64)
    print(f"\n🔍 Verification Result:\n{result}")