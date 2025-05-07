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

Here is my python code.

- [AES_encrypt](Python_Source/aes_encrypt.py) 
- [AES_decrypt](Python_Source/aes_dencrypt.py)

#### Encrypt the plaintext :

Ezekiel will encrypt a secret message using his key then give to me.

![aes_e](screenshot/aes_e.png)

#### Decrypt the ciphertext :

Now let's decrypt the ciphertext.

![aes_d](screenshot/aes_d.png)

---

### ✅ Task 2: Asymmetric Encryption (RSA)

Here is my python code.

- 
- [RSA_decrypt](Python_Source/rsa_decrypt.py)
- [RSA_key_generator](Python_Source/rsa_key_generator.py)


#### generate key pairs :

I will create a key pairs wich is `private key` **(not to share)** and `public key` **(share to Kiel)**.

![rsa_key_generator](screenshot/rsa_key_generator.png)


#### Encrypt the plaintext :



#### Decrypt the ciphertext :

![rsa_decrypt](screenshot/rsa_decrypt.png)

---

### ✅ Task 3: Hashing (SHA-256)

- Generate SHA-256 hash of input strings and files.
- Multiple inputs shown.
- 🔗 [View Code](task3_hashing/sha256_hashing.py)
- 🖼️ Screenshots: [hashing_screenshots](task3_hashing/hashing_screenshots/)

---

### ✅ Task 4: Digital Signatures (RSA)

- Message signing using private key.
- Signature verification using public key.
- 🔗 [View Code](task4_digital_signature/digital_signature.py)
- 🖼️ Output: `signature_verification.png`

---

