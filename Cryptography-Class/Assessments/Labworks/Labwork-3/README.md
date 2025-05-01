# 🔐 Lab 3: Hands-on Exploration of Cryptographic Tools (OpenSSL)

Muhammad Aabas Bin Md Suji
-My partner is Ezekiel
---

## 🧠 Lab Objectives

This lab introduces students to OpenSSL, a powerful open-source cryptographic toolkit. Students will explore core cryptographic operations including:

- Symmetric encryption (AES)
- Asymmetric encryption (RSA)
- Hashing (SHA-256)
- Digital signatures (RSA + SHA-256)

### Upon Completion, You Will Be Able To:

✅ Encrypt and decrypt files using symmetric and asymmetric methods  
✅ Generate and verify data hashes  
✅ Create and verify digital signatures

---

## 🧩 Lab Tasks

You are required to research and use correct `OpenSSL` commands to:

1. **Symmetric Encryption** – using AES
2. **Asymmetric Encryption** – using RSA keys
3. **Hashing** – using SHA-256
4. **Digital Signatures** – sign and verify using RSA + SHA-256

---

## Task 1 : Symmetric Encryption and Decryption using AES-256-CBC

### Tools Used :
- Openssl

### Step-by-step :

#### Step 1 :
I am a `reciever` and `Kiel` is a `sender`. He will create a plaintext and key then send to me the encrypted message.

#### Plaintext :
```bash
echo "flag{AES_256_CBC}" > kiel_aes.txt
```
![aes_p](screenshot/aes_ss/rsa_ss/plaintext.png)

#### Cyphertext :
```bash
openssl enc -aes-256-cbc -salt -in kiel_aes.txt -out kiel_aes.enc -k abc123
```
![aes_e](screenshot/aes_ss/rsa_ss/encrypt.png)

- `openssl` - Tells OpenSSL to use its encryption function
- `-aes-256-cbc` -Specifies the AES encryption algorithm with a 256-bit key in CBC (Cipher Block Chaining) mode.
- `-in` - Specifies the input file to be encrypted
- `-out` - Specifies the output file where the encrypted data will be stored
- `-k` - Uses the password `abc123` to generate the encryption key

Now Kiel will send the message and pub key to me.

---

#### Step 2 :
After I recieve the message and key from email, lets dencrypt the cyphertext using `abc123` as key.

#### Commands :
```bash
openssl enc -d -aes-256-cbc -in kiel_aes.enc -out kiel_aes.txt 
```
![aes_d](screenshot/aes_ss/rsa_ss/aes_d.jpg)

- `-d` - tells openssl to decrypt the cyphertext

#### Results :
![aes_r](screenshot/aes_ss/rsa_ss/aes_r.jpg)

flag{AES_256_CBC}

---

## Task 1 : Symmetric Encryption and Decryption using AES-256-CBC



## 📌 Notes

This repository is part of my journey to mastering cryptography fundamentals using real tools like OpenSSL. It serves both as a study reference and demonstration of hands-on competency.

---

