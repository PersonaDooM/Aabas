# GPG & SSH Key Management + Hash Cracking Tasks

**Name:** Muhammad Aabas Bin Md Suji  
**Email:** maabas.mdsuji@student.gmi.edu.my  
**Student ID:** NWS23010046  

## 📌 Overview

This repository contains the results and evidence of five key tasks involving GPG key management, file encryption/decryption, digital signing, passwordless SSH configuration, and hash cracking. These tasks were carried out as part of the cybersecurity learning module.

---

## ✅ Task 1: Generate GPG Key Pair

### Create RSA key pair 

Generate key with `gpg`.

```bash
gpg --full-generate-key
```

- `--full-generate-key`: This tells GPG to guide you through a detailed key creation process.

![alt text](screenshot/Task_1/create_key.png)

- **Key Type:** RSA & RSA  
- **Key Size:** 4096 bits  
- **Expiry:** 1 year

#### Name:

![alt text](screenshot/Task_1/name_key.png)

**After create a key, `gpg` will ask us to put a password for the key.*

---

### Result

List key in `gpg`.

```bash
gpg --list-keys
```

![alt text](screenshot/Task_1/list_key.png)

---

## ✅ Task 2: Encrypt and Decrypt a File


### Create plaintext

```bash
echo "This file was encrypted by Aabas (NWS23010046)" > plaintext.txt
```

---

### Encrypt plaintext

```bash
gpg --encrypt --recipient maabas.mdsuji@student.gmi.edu.my plaintext.txt
```

![alt text](screenshot/Task_2/encrypt.png)

- `--recipient` : gpg will find the key that has binded with the email like key id.

*after encrypt.

```bash
gpg: encrypted with 4096-bit RSA key, ID BA006ABD5FF03EB9, created 2025-05-16
      "Muhammad Aabas Bin Md Suji (Practical_test_1) <maabas.mdsuji@student.gmi.edu.my>"
```

---

### Decrypt ciphertext

```bash
gpg --output decrypted.txt --decrypt plaintext.txt.gpg
```

![alt text](screenshot/Task_2/decrypt.png)

- `--outout` : make a output from decryption.

Then we need to enter the password.

---

### Result

![alt text](screenshot/Task_2/output.png)

---

## ✅ Task 3: Sign and Verify a Message


