# 🔐 Lab 2: Cryptographic Attacks – Cracking Weak Password Hashes & Exploiting Poor Authentication in Databases

**👨‍💻 Author**: Raja Muhammad Haiqal Shah Bin Raja Muzairil Shah  
**📅 Date**: 25 April 2025  
**⏳ Time Allocation**: 3 Hours  
**📝 Total Marks**: 15  
**🧩 Lab Type**: Hands-On + Report + Demo/Debrief  

---

## 🧠 A. Lab Objectives

1. Identify and exploit cryptographic weaknesses in database authentication and password storage.
2. Perform offline hash cracking after discovering password hashes in a vulnerable database.
3. Investigate real-world cryptographic failures and propose secure solutions.
4. Document findings clearly in GitHub (Markdown) and present a short demo/debrief.

---

## 🛠️ Tools Used

- `Kali Linux` (OS)
- `nmap` (Service enumeration)  
- `mysql-client` (Database access)  
- `hashid` / `hash-identifier` (Hash detection)  
- `hashcat` / `john` (Hash cracking)  
- `wireshark` (Traffic analysis – optional)

---

## 🌐 IP Addresses

- **Attacker**: `192.168.157.142`  
- **Victim**: `192.168.157.137`  

---

## 🧩 B. Lab Tasks

### 1. 🔍 Service Enumeration and Initial Access

**Command Used:**

```bash
nmap -sV -p 3306 192.168.157.137 > nmap.txt

```
![nmap](screenshot/nmap_scan.png)

- Identified that **MySQL** was running on port **3306**.

**Attempting Connection:**

```bash
mysql -h 192.168.157.137 -u root --password=""
```

**Error Encountered:**
```vbnet
ERROR 2026 (HY000): TLS/SSL error: wrong version number
```

**Solution:**

```bash
mysql -h 192.168.157.137 -u root --password="" --ssl=0
```

![fix command](screenshot/fix_command.png)

✅ **Resolved**: TLS version mismatch between MySQL client and server.

> **Note**:  
> MySQL versions prior to 5.7.11 do not support `--ssl-mode`. Use `--ssl=0` to disable SSL.

---

### 2. 🧑‍💻 Enumeration of Users and Authentication Weaknesses

```sql
USE dvwa;
SHOW TABLES;
```

**Expected Output:**

```diff
+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      |
| users          |
+----------------+
```
**Querying user data:**
```sql
SELECT * FROM users;
```

- Found usernames and MD5 password hashes.
- Selected user admin for cracking.

![usernpass](Screenshots/usernpass.png)

**Saved hash to file:**

```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
```

> ⚠️ **Reflection Question**:  
> Is accessing a database with no password a cryptographic failure?  
> ✅ **Yes**. It violates secure authentication practices by allowing unauthorized access due to missing or weak credentials.

---

### 3. 🔍 Password Hash Discovery & Identification

Used `hash-identifier`:

```bash
hash-identifier 5f4dcc3b5aa765d61d8327deb882cf99
```

- Detected as **MD5** hash.

![hashidentifier](Screenshots/hashidentifier.png)

> ⚠️ **Reflection Question**:  
> What cryptographic weaknesses exist in this hashing method?  
> - MD5 is **unsalted** and **fast**, making it susceptible to rainbow table and brute-force attacks.

---

### 4. 🧨 Offline Hash Cracking

Used **hashcat** to brute-force the MD5 hash:

```bash
hashcat -m 0 hash.txt --show > cracked_results.txt
```

✅ **Result:**
```text
5f4dcc3b5aa765d61d8327deb882cf99:password
```

![hashcatresult](Screenshots/hashcatresult.png)

**Cracked Password**: `password`

> Password entropy is low. "password" is one of the most common weak passwords.

---

### 5. 🔐 Cryptographic Analysis & Mitigation

#### 🔎 Identified Weaknesses:

| Component     | Issue                         |
|---------------|-------------------------------|
| Authentication | Empty/Weak passwords          |
| Hashing        | MD5 without salt              |
| Transmission   | Plaintext over network        |

#### 🔧 Recommendations:

- **Authentication**: Enforce strong password policies, apply rate-limiting or use `fail2ban`.
- **Hashing**: Replace MD5 with **bcrypt** or **Argon2** (both are memory-hard and slow).
- **Transmission**: Enable **SSL/TLS** encryption for database connections.

#### 🕵️ Wireshark Observation:

Captured raw data during database login. Password hashes and queries visible in plaintext.

![wireshark](Screenshots/wirehark.png)

---

## ✅ Conclusion

This lab demonstrated real-world cryptographic vulnerabilities that still exist in poorly configured systems. Weak authentication, outdated hashing, and unencrypted transmissions can all be exploited easily by attackers.

Securing such systems involves:
- Enforcing authentication best practices,
- Adopting strong, salted password hashing,
- Ensuring secure encrypted communication channels.

**Always audit legacy systems for these cryptographic flaws.** 🔐

---

🧠 *"Attack like a black hat. Defend like a white hat."* – Haiqal