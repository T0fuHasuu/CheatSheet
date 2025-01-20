T0fuHasuu
---

# **Pickle Rick Walkthrough**  
[**Source**](https://whokilleddb.medium.com/tryhackme-pickle-rick-walkthrough-2c33bf07c77b)  

![Chill](https://i.pinimg.com/originals/24/97/5b/24975bccb319c0bb62e36ff9e20d0c93.gif)  

---

### **1. Scan for Open Ports with Nmap**
Run the following command to scan the target IP:  
```bash
nmap <IP>
```

- **Results:**  
  - Port **22**: SSH  
  - Port **80**: HTTP  

---

### **2. Explore the Website (Port 80)**  
Visit the website:  
```bash
http://<IP>
```

- Inspect the **source code** to find **R1ckRul3s** (likely a username).  
- Check for a `robots.txt` file:  
  ```bash
  curl http://<IP>/robots.txt
  ```
  - This reveals some "wobbling" text, potentially the password.  

---

### **3. Check the /assets Directory**  
Access the assets directory:  
```bash
http://<IP>/assets
```

- Examine subdirectories:  
  - You'll find **portal.jpg**.  
- Use **gobuster** to uncover additional directories:  
  ```bash
  gobuster dir -u http://<IP> -w <wordlist>
  ```
  - Locate the `/portal.php` directory.  
- Use the discovered **username** and **password** to log in.  

**Outcome:** You’ll reach a command execution page.  

---

### **4. Execute Commands**  
- Use `ls` to list available files.  
- Identify a strange file name with a `.txt` extension.  
- Access the file via:  
  ```bash
  http://<IP>/<StrangeFileName>.txt
  ```

---

### **5. Investigate PHP Configurations**  
Run the following to search for potential exploits:  
```bash
grep -R ""
```

- Inspect the source code of the results.  
- Check if there are **sudo privileges** for the root user:  
  ```bash
  sudo -l
  ```
  - If unrestricted, gain root access!  

---

### **6. Find the Flags**  
Once root access is achieved:  

1. List directories to locate flags:  
   ```bash
   sudo ls ../../../*
   ```  
2. Flags found:  
   - **Second Flag:** `/home/rick/second ingredients`  
   - **Third Flag:** `/root/3rd.txt`  

---

![Sayonara](https://media.tenor.com/WC3Hil6PFD8AAAAM/capybara-riding.gif)  

---  

# Peace out . . .