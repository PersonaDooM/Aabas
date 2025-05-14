# 🔐 Lab 1: Cryptographic Attacks — Brute Force and Traffic Analysis on Network Protocols

## 🎯 Objectives

- Understand how brute-force attacks work on common network services (FTP, Telnet, SSH).
- Practice using tools like Hydra for password attacks.
- Learn how to use Wireshark to analyze network traffic.
- Identify insecure protocols that transmit data in plaintext.
- Propose secure alternatives and mitigation strategies.

---

## 🧰 Setup

- **Hydra** & **Medusa** – for performing brute force attacks  
- **Wireshark** – for capturing and analyzing network traffic  
- **Kali Linux** – used as the attacker machine  
- **Metasploitable2** – vulnerable virtual machine  
- **FTP, Telnet, SSH** – services used for login and analysis
  
Kali Linux : 192.168.157.145
Metasploitable : 192.168.157.137

---

## 🔍 Service Discovery (Optional Enumeration Step)

Use Nmap to identify running services on the target:

```bash
nmap -sV -p 21,22,23,80 192.168.157.137
```
![nmap](screenshot/nmap.png)

### Explanation:
- `-sV`: Version detection (shows service version like vsftpd, OpenSSH)
- `-p`: Specifies ports to scan (21 = FTP, 22 = SSH, 23 = Telnet, 80 = HTTP)
  
Result:  
- FTP running on port 21  
- Telnet on port 23  
- SSH on port 22
- HTTP on port 80

---

## Discover Venerable Username & Password

## 1. Enumeration of Usernames🥐

Prepare a list of potential usernames and passwords to use for brute-force attacks.

### 1.1 Create a text file for usernames:

![username](screenshot/nmap.png)

### 1.2 Create a text file for passwords:

![password](screenshot/password.png)

---