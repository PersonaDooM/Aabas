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

---

### ✅ Task 3: Hashing (SHA-256)

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

---

### ✅ Task 4: Digital Signatures (RSA)

- Message signing using private key.
- Signature verification using public key.
- 🔗 [View Code](task4_digital_signature/digital_signature.py)
- 🖼️ Output: `signature_verification.png`

---

