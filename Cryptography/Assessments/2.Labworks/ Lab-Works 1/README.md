# 🧪 Lab 1: Cryptographic Attacks - Brute Force & Traffic Analysis on Network Protocols

**Name**: Adli Jaafar  
**Date**: March 18 (Edited April 9)  
**Points**: 15  
**Time Allocated**: 3 Hours  

---

## 🧠 Objective

This lab explores the weaknesses of network protocols (FTP, TELNET, SSH, HTTP) by performing brute force attacks to recover user credentials. Using these credentials, we sniff and analyze traffic to identify protocols transmitting data insecurely, and propose more secure alternatives.

---

## 🛠️ Tools Used

- Hydra
- Medusa
- NetExec
- Burp Suite (Intruder)
- Wireshark
- tcpdump
- Kali Linux (Attacker Machine)
- Vulnerable VM (Target Machine)

---

## 🔎 1. Username Enumeration

**Goal**: Identify potential usernames for brute force attempts.

### 🔧 Methods Used:
- Used `enum4linux`, `rpcclient`, and `NetExec` to enumerate users on the vulnerable VM.

### 🔍 Discovered Usernames:
