# 🔐 Lab 4: Implementing Cryptography with Python

**Name** : Muhammad Aabas Bin Md Suji     **My partner** : Ezekiel

---

## 🧠 Objectives

This lab covers:

- Symmetric Encryption using AES
- Asymmetric Encryption using RSA
- Hashing using SHA-256
- Digital Signatures using RSA

---

## 🔨 Tools
Here I'm using `Visual Studio Code` for my platform to run python code.

> How to use `VS Code`?

#### Step 1 :
install python from extensions

#### Step 2 :
Open terminal in vscode and install `pycryptodome`.

```bash
pip install pycryptodome
```

- If error, It will give the right command then use full quotes in PowerShell. Example :
```powershell
& "C:/Users/aabas/AppData/Local/Programs/Python/Python312/python.exe" -m pip install pycryptodome
```

Now our `visual studio code` is ready to use.

---
## 🧩 Tasks Overview

### ✅ Task 1: Symmetric Encryption (AES)

### 🔐 What is AES?
- AES (Advanced Encryption Standard) is a way to securely encrypt and decrypt data using a secret key.

Here is my python code.

- [AES_encrypt](Python_Source/aes_encrypt.py) 
- [AES_decrypt](Python_Source/aes_dencrypt.py)

#### Encrypt the plaintext :

Ezekiel will encrypt a secret message using his key then give to me.

![aes_e](screenshot/aes_e.png)

#### Decrypt the ciphertext :

Now let's decrypt the ciphertext.

![aes_d](screenshot/aes_d.png)

### 💡 Explanation

- `Generate a key` – like a password, used to lock/unlock data.
- `Encrypt` – turns your message into scrambled text.
- `Decrypt` – turns the scrambled text back into the original message.

---

### ✅ Task 2: Asymmetric Encryption (RSA)

### 🔐 What is RSA?

RSA is a method for encrypting and decrypting data using two keys:

- Public key (used to encrypt)
- Private key (used to decrypt)

Here is my python code.

- [RSA_encrypt](Python_Source/rsa_encrypt.py)
- [RSA_decrypt](Python_Source/rsa_decrypt.py)
- [RSA_key_generator](Python_Source/rsa_key_generator.py)


#### generate key pairs :

I will create a key pairs wich is `private key` **(not to share)** and `public key` **(share to Kiel)**.

![rsa_key_generator](screenshot/rsa_key_generator.png)


#### Encrypt the plaintext :

Kiel will encrypt a `plaintext` to `ciphertext` using my `public key` then send back to me.

![rsa_encrypt](screenshot/rsa_encrypt.png)

#### Decrypt the ciphertext :

I will decrypt the `ciphertext` using my `private key` to see the plaintext.

![rsa_decrypt](screenshot/rsa_decrypt.png)

### 💡 Explanation

- `Generate key pair` – creates a private and public key.
- `Encrypt with public key` – only the private key can decrypt this.
- `Decrypt with private key` – gets the original message back.

---

### ✅ Task 3: Hashing (SHA-256)

### 🔐 What is SHA-256?

SHA-256 is a one-way hashing algorithm that turns data into a fixed-size string (digest). It's commonly used to verify data integrity (not for encryption/decryption).


Here is my python code.

- [SHA-256_script](Python_Source/sha256_hash.py)

#### Hashing the message :

![sha256 hash](screenshot/sha256_hash.png)

#### Edit the message :

Add `-` to the end of the message to see the hash output.

![sha256 edit](screenshot/sha256_edit.png)

#### Result :

First hash : Cryptography Lab by Muhammad Aabas [DooM]  > NWS23010046 !
```bash
01a46a1976295b75af5c79c9217d9d5cefc35aa5d34d29a742b26d98e95fe99f
```

Second hash : Cryptography Lab by Muhammad Aabas [DooM]  > NWS23010046 !-
```bash
82f4940910b19700f28ed6a578d4af037833a5d2fd6f0da198cc84dd88d68fe6
```

### 🌪️ What is the Avalanche Effect?
When you change even 1 character (or 1 bit) in the input, the entire hash output changes drastically — like a chain reaction.

### 🔍 Why Does It Happen?

Hash functions are designed so that:

- Tiny changes in input produce completely different hashes
- You can’t guess the input from the hash
- It’s impossible to predict how the output will change

This makes hash functions very secure and perfect for:

- `Password storage`
- `File integrity checking`
- `Digital signatures`

---

# 🔐 Task 4: Digital Signatures (RSA)

## ✍️ What is a Digital Signature?

A digital signature guarantees:

- ✅ **Integrity** – The message was not altered.
- ✅ **Authenticity** – The message truly came from the private key owner.

### 🧠 How It Works:

1. The sender **signs** the message using their `private key`.
2. The receiver **verifies** the signature using the sender's `public key`.

---

## 🛠️ Python Code

- 📄 [`sign_generator.py`](Python_Source/sign_generator.py) – generates the digital signature  
- 📄 [`sign_verify.py`](Python_Source/sign_verify.py) – verifies the digital signature

---

## ✉️ Steps

### 1️⃣ Generate & Sign Message

Use your `private key` (from **Task 2**) to sign a message and send both the message and the signature to **Kiel**.

📸 Screenshot:  
![sign create](screenshot/sign_create.png)

---

### 2️⃣ Verify the Message

**Kiel** uses your `public key` to verify that the message and signature are valid and unchanged.

📸 Screenshot:  
![sign valid](screenshot/sign_valid.png)

---

### 3️⃣ Modify the Message

If even a small change is made to the message, verification will fail — demonstrating tamper detection.

📸 Screenshot:  
![sign invalid](screenshot/sign_invalid.png)

---

## ✅ Summary

🔒 Digital signatures are strict by design:

- The message, key, padding, and hash **must match exactly**.
- Even the slightest change causes `.verify()` to fail.
- This behavior ensures strong protection against tampering or corruption.

---

## 💡 Function Breakdown

- 🔐 `private_key.sign()` → Signs the message (only the private key holder can do this).
- 🔓 `public_key.verify()` → Confirms the message hasn't been altered and matches the original signature.



---

```bash
If you have question, you can contact me 😉
```