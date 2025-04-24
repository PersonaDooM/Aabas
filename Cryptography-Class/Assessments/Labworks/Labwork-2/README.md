# 🔐 Lab 2: Cryptographic Vulnerabilities and Attacks on Weak Password Storage

**Author:** [Your Name]  
**Date:** [Insert Date]  
**Course:** Cryptography Class

---

## 🧭 Lab Overview

In this lab, we’ll simulate a real-world cryptographic attack involving the discovery and exploitation of weak password storage mechanisms. You’ll learn how attackers extract and crack password hashes from vulnerable systems, and understand the importance of secure authentication practices.

---

## 🎯 Objectives

- Identify exposed user credentials and insecure password storage in a vulnerable database.
- Detect the type of hash algorithm used to store the passwords.
- Perform an offline hash cracking attack using tools such as `hashcat` or `john`.
- Evaluate weaknesses in authentication implementations and recommend improvements.
- Document findings clearly with supporting visuals and explanations.

---

## 🛠 Tools & Environment

| Tool           | Purpose                           |
|----------------|-----------------------------------|
| Kali Linux     | Attacker machine                  |
| MySQL Client   | Connecting to target database     |
| Nmap           | Network scanning                  |
| Hash-Identifier / HashID | Detecting hash types     |
| John the Ripper / Hashcat | Password cracking      |
| Wireshark (Optional) | Packet capture (if needed)  |

---

## 🌐 Lab Network Setup

- **Attacker IP:** `192.168.157.142` (Kali Linux) 
- **Target IP:** `192.168.157.137` (Metasploitable2)

Ensure both virtual machines are on the same NAT/Bridged network to interact properly.

---

## 📌 Step-by-Step Instructions

### 🔍 Step 1: Scanning the Target

Scan open ports on the target system using `nmap`.

```bash
nmap -sS -sV -T4 192.168.157.137

![!\[alt text\](nmap_scan.png)](./screenshot/nmap_scan.png)