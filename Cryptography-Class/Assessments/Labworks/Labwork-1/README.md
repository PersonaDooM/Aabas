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

![username](screenshot/username.png)

### 1.2 Create a text file for passwords:

![password](screenshot/password.png)

---

## 2. Brute Force Attacks🥖

### 2.1 FTP
- **Tool**: Medusa
- **Command**:

```bash
hydra -L usernames.txt -P passwords.txt ftp://192.168.154.133
```

### Explanation:
- `-h`: Target IP address.
- `-U`: Username wordlist.
- `-P`: Wordlist.
- `-M`: Service that we want to do.
- `-t`: boost brute-force speed.

![ftp](screenshot/ftp_b.png)

**Result**: Successful login found – `msfadmin:msfadmin`


---

### 2.2 Telnet
- **Tool**: Hydra
- **Command**:

```bash
hydra -l msfadmin -P passwords.txt telnet://192.168.157.137
```

### Explanation:
- `-l`: Specify a single username.
- `-P`: Load a list of passwords from a file.
- `telnet://`: Specifies the Telnet service and target IP.

![telnet](screenshot/telnet_b.png)


**Result**: Successful login – `msfadmin:msfadmin`


---

### 2.3 SSH
- **Tool**: Medusa
- **Command**:

```bash
medusa -h 192.168.157.137 -U usernames.txt -P passwords.txt -M ssh
```
### Explaination
- `-h`: Target host (your Metasploitable IP)
- `-U`: File containing usernames
- `-P`: 	File containing passwords
- `-M`: Module to use – in this case, ssh for brute-forcing SSH login
  
![ssh_b](screenshot/ssh_b.png)

Results: ACCOUNT FOUND: [ssh] Host: 192.168.204.147 User: msfadmin Password: msfadmin [SUCCESS]

---

### 2.4 HTTP

#### Step 1

Open Browser and put metasploitable2 ip address in the url.

```bash
192.168.157.137
```

![browser](screenshot/open_browser.png)

after that, open dvwa and login then go to brute-force page.

![dvwa](screenshot/dvwa.png)

---

### Step 2

open burpe suite and go to proxy then on the intercept.

![burpe suite](screenshot/burpe_suite.png)

---

### Step 3

login the dvwa with the wrong password then burpe suite will intercept the request from website.

![capture](screenshot/capture.png)

### Step 4

right click the request then send the request to introder.

![send_to_intruder.png](screenshot/send_to_intruder.png)

### Step 5

Here, highlight the username and password that we put and click add. After that change attack type to cluster bomb attack.

![](screenshot/cluster_bomb_attack.png)

### Step 6

In payload session, put wordlist for password and username.

Username :

![!\[alt text\](image.png)](screenshot/username_payload.png)

Password :

![!\[alt text\](image.png)](screenshot/password_payload.png)

After that click `Start Attack`.

---

### Result :

In the result, we can verify the longest length is the real username and password.

![!\[alt text\](image.png)](screenshot/result.png)

![!\[\](image.png)](screenshot/open_result.png)

Now copy the request and over write the previous request in the proxy then click `forward`.You will successful login to the dvwa brute force form.

![!\[alt text\](2025-05-15 020109.png><Screenshot )](screenshot/success.png)

**Welcome to the password protected area admin*

---

## 3. Sniffing Network Traffic🍖

### 3.1 Start Wireshark
 
 Open wireshark then choose `eth0` to capture real-time traffic.

![ !\[alt text\](image.png)](screenshot/wireshark.png)

---

### 3.2 Capture FTP

Login Metasploitable2 via ftp from kali with the discovered username and password.

```bash
ftp 192.168.157.137
```

![!\[alt text\](image.png)](screenshot/login_ftp.png)

Open wireshark open follow tcp stream on `ftp` packet.

![!\[alt text\](image.png)](screenshot/capture_ftp.png)

---

### 3.3 Capture TELNET

Login Metasploitable2 via TELNET from kali with the discovered username and password.

```bash
telnet 192.168.157.137
```

![!\[alt text\](image.png)](screenshot/login_telnet.png)

Open wireshark open follow tcp stream on `telnet` packet.

![!\[alt text\](image.png)](screenshot/capture_telnet.png)

---

### 3.4 Capture SSH

Login Metasploitable2 via SSH from kali with the discovered username and password.

error:

```bash
ssh msfadmin@192.168.157.137
```

correct:

```bash
ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa msfadmin@192.168.157.137
```

- `-oHostKeyAlgorithms=+ssh-rsa` -  Allows the client to accept a server's `ssh-rsa` host key.
- `-oPubkeyAcceptedKeyTypes=+ssh-rsa` - Tells the client to accept `ssh-rsa` public keys from the server for authentication.

#### 💡 Why the Issue Happens
- The server is outdated (like Metasploitable2), and only supports legacy cryptographic algorithms.
- Your client is secure and modern, refusing to use old, broken standards unless you explicitly permit them.

![!\[alt text\](image.png)](screenshot/login_ssh.png)

Open wireshark open follow tcp stream on `ssh` packet.

![!\[alt text\](image.png)](screenshot/capture_ssh.png)

---

## 4. Problems Encountered🍕

| Protocol | Problem | Solution |
|----------|---------|----------|
| FTP      | None    | N/A      |
| Telnet   | Service was off initially | Enabled Telnet on Metasploitable2 |
| SSH      | Hydra connection failed due to key mismatch or outdated program | Use Hydra |

---

## 5. Mitigation Strategies🍥

| Protocol | Vulnerability | Secure Alternative | Why it’s better |
|----------|---------------|--------------------|-----------------|
| FTP      | Sends credentials in plaintext | SFTP / FTPS | Encrypts file transfer data and credentials |
| Telnet   | Transmits all in plaintext | SSH | SSH encrypts communication |
| SSH      | Still brute-forceable | Use key-based login, strong passwords | Prevents brute force access |
| HTTP     | Data sent in Plaintext | HTTPS | Data is encrypted |

---

## ✅ Summary

- FTP and Telnet are insecure protocols that transmit credentials in plaintext.
- Hydra can easily brute-force weak credentials.
- SSH is secure but can still be targeted using brute-force unless hardened.
- Use tools like Wireshark to confirm data security over the network.
- Always replace insecure services with encrypted alternatives like SSH or FTPS.
- Apply proper access control, firewalls, and monitoring to reduce attack surfaces.

---