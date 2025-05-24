from Crypto.Cipher import AES
from hashlib import sha256
import os

# 1. Key setup
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"  # "BukanRahsiaLagi"
KEY = sha256(KEY_STR.encode()).digest()[:16]

# 2. Padding remover
def unpad(data):
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError("Invalid padding length")
    return data[:-pad_len]

# 3. Decrypt function
def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)

    # Output to new file
    output_path = output_file = filepath.replace(".txt.enc", ".txt")

    with open(output_path, "wb") as f:
        f.write(plaintext)
    print(f"[+] Decrypted: {output_path}")




# 4. Main process
if __name__ == "__main__":
    folder = r"C:\Users\aabas\OneDrive - Accord Investments\Documents\GitHub\Aabas\Cryptography-Class\Assessments\Assignment\Practical_test\Practical_test_2\locked_files"

    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            path = os.path.join(folder, filename)
            try:
                decrypt_file(path)
            except Exception as e:
                print(f"[-] Failed to decrypt {filename}: {e}")

if not os.path.exists(folder):
    print(f"[-] Folder '{folder}' tidak wujud!")
exit(1)
