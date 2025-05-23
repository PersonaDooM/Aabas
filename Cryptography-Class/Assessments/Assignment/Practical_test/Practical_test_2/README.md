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

---

### 🔎 1. Analysis with VirusTotal

Open `VirusTotal` in hte browser then analys the file.


> photo

- We need to identify if the file is save or not.

---

### 🔎 2. Static Analysis with DIE

Open `DIE` and upload the file to see the structure.

> Use DIE to identify how the `.exe` file was packed or compiled.

```text

```

Result:
- File Type: PE32 executable
- Compiler: PyInstaller v3.6
- Entropy: Medium

**Why this is important:**
Knowing that PyInstaller was used helps us decide the correct extractor tool (`pyinstxtractor`) to use.

**Possible Errors:**
- ❌ *Unknown compiler* → The file may be obfuscated or not made with PyInstaller.
- ✅ *Solution:* Try running `strings malware.exe | findstr PyInstaller` to confirm manually.

---

### 📦 3. Extract with pyinstxtractor

**Purpose:**  
Extract the compiled Python bytecode files from the `.exe`.

```bash
python pyinstxtractor.py malware.exe
```

**Expected Output:**

A folder named `malware.exe_extracted/` will be created.
Inside it: `malware.pyc`, possibly other `.pyc` files.

**Why this is important:**
We need .pyc files to decompile and view the original code logic.

Possible Errors:

- ❌ “Invalid PyInstaller archive” → The `.exe` file may be encrypted, corrupted, or not PyInstaller.
- ✅ Solution: Confirm version using DIE and try adjusting `pyinstxtractor.py` manually (specify version).
- ❌ Python version mismatch → If pyinstxtractor fails silently.
- ✅ Solution: Use Python 3.8 as most PyInstaller v3 apps work with it.

---

### 🔓 4. Decompile .pyc to .py

Convert `.pyc` files back into readable `.py` source code.

```bash
uncompyle6 -o . __main__.pyc
```

Reading the Python source helps us understand the malware’s behavior and find encryption logic.

**Possible Errors:**

- ❌ “Unsupported magic number” → The .pyc was made with an incompatible Python version.
- ✅ Solution: Try another version of Python for decompilation (3.7, 3.9).
- ❌ “Decompilation failed” → The bytecode is malformed or obfuscated.
- ✅ Solution: Try decompyle3 or use online decompilers.

---

## 🧠 Code Analysis

#### 🔐 Identified AES Encryption Code:

Identify how AES was used and what values (key, IV, ciphertext) are involved.

```python
```

This gives us the information we need to write a decryption script.

---

## 🧬 Reverse Engineering Objective

The goal is to write a `decryption script` to get the `original plaintext`.

#### Decryption Script:

```python

```

This proves you understood and reversed the malware’s encryption mechanism.

---

## 🧾 Result




---

## 🧠 Conclusion

- The malware used `AES CBC` encryption to obfuscate its payload
- Static + dynamic analysis allowed retrieval of the original message
- This task demonstrates basic reverse engineering and cryptography understanding
