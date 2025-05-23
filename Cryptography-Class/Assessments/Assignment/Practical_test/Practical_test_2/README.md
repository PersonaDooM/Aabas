# 🔬 Malware Analysis Report – Python-based Executable with AES Encryption

## 📝 Task Description

This task involves analyzing a Python-based malware sample compiled into a `.exe` file. The goal is to:
- Decompile the `.exe` into readable Python code
- Identify AES encryption logic
- Reverse-engineer the code to create a decryption script
- Retrieve the original plaintext from the given ciphertext

---

## 🧰 Tools Used

See the guides to install the tools [here.](requirement/README.md)

| Tool            | Purpose                                   |
|-----------------|-------------------------------------------|
| `Python 3.8`      | Required version for compatibility        |
| `DIE (Detect It Easy)` | Determine how the malware was compiled |
| `pyinstxtractor`  | Extract `.pyc` files from PyInstaller `.exe` |
| `uncompyle6`      | Decompile `.pyc` files to readable `.py`  |
| `VS Code `        | Code editor for analysis                  |

---

## 📁 Initial File

- `malware.exe` – suspected to be compiled with PyInstaller

---

## 🔍 Step-by-Step Analysis

### 🔎 1. Analysis with VirusTotal

Open `VirusTotal` in hte browser then analys the file.


> photo

---

### 🔎 2. Static Analysis with DIE

Open `DIE` and upload the file to see the structure.

```text

```

Result:
- File Type: PE32 executable
- Compiler: PyInstaller v3.6
- Entropy: Medium

---

### 📦 3. Extract with pyinstxtractor

```bash
python pyinstxtractor.py malware.exe
```



---

### 🔓 4. Decompile .pyc to .py

```bash
uncompyle6 -o . __main__.pyc
```

---

## 🧠 Code Analysis

#### 🔐 Identified AES Encryption Code:



---

## 🧬 Reverse Engineering Objective

The goal is to write a `decryption script` to get the `original plaintext`.

#### Decryption Script:

```python

```

---

## 🧾 Result




---

## 🧠 Conclusion

- The malware used `AES CBC` encryption to obfuscate its payload
- Static + dynamic analysis allowed retrieval of the original message
- This task demonstrates basic reverse engineering and cryptography understanding
