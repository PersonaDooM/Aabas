from Crypto.PublicKey import RSA
import base64

def generate_rsa_keys():
    # Generate RSA key pair (2048-bit key)
    key = RSA.generate(2048)
    
    # Extract the public and private keys
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    # Convert keys to Base64
    private_key_b64 = base64.b64encode(private_key).decode('utf-8')
    public_key_b64 = base64.b64encode(public_key).decode('utf-8')
    
    return public_key_b64, private_key_b64

if __name__ == "__main__":
    public_key_b64, private_key_b64 = generate_rsa_keys()
    
    print("Public Key (Base64):")
    print(public_key_b64)
    
    print("\nPrivate Key (Base64):")
    print(private_key_b64)
