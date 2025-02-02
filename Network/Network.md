# **Network Security Summary & Key Points**  

## **1. Internet & Network Communication**  
- The internet consists of multiple routers (ISPs) that transmit data between users.  
- **SSL/TLS**: A protocol ensuring secure communication.  
- **HTTP**: Handles requests like GET and POST from websites.  
- **HTTPS**: A secure version of HTTP, protected by SSL/TLS.  
- **VPN**: Encrypts data and masks the user's IP address to appear from another location.  

## **2. SSL/TLS Security Features**  
- **Confidentiality**: Encrypts data, accessible only to client & server.  
- **Integrity**: Uses hashing to prevent modification of data.  
- **Authentication**: Utilizes PKI to prevent impersonation attacks.  

### **Anti-Replay Protection**  
- Prevents reuse of captured data packets to avoid duplication attacks.  

### **Non-Repudiation**  
- Ensures sent messages cannot be modified, making the sender fully responsible.  

## **3. Key Players in Secure Communication**  
- **Client**: Initiates the TLS handshake (not authenticated).  
- **Server**: Receives the TLS handshake (always authenticated).  
- **Certificate Authority (CA)**:  
  - Acts as a **Trust Anchor** by issuing certificates to websites, ensuring they are legitimate.  

### **TLS 1.3 Enhancements**  
- Shorter handshake for improved speed.  
- 0-RTT resumption for faster reconnections.  
- **Forward Secrecy**: Protects past communications even if encryption keys are compromised.  
- Uses only **AEAD ciphers** and removes insecure algorithms.  

## **4. Cryptographic Hashing**  
- Converts an original message into a fixed-length fingerprint.  
- Properties:  
  - One-way function (irreversible).  
  - Small changes drastically alter output.  
  - Outputs are always of fixed length.  
  - **Collisions** (same hash for different inputs) are rare but possible.  

### **Common Hashing Algorithms**  
- **MD5** – 128-bit (Weak, not recommended).  
- **SHA-1** – 160-bit (Weak, not recommended).  
- **SHA-2 Family** (More Secure): SHA-224/256/384/512-bit.  

## **5. Data Integrity & Authentication**  
- Ensures messages remain unchanged during transmission.  
- **Message Authentication Code (MAC)**: Uses a secret key to verify data integrity.  
  - **HMAC**: Uses hashing algorithms (MD5, SHA) for added security.  

## **6. Encryption Techniques**  
### **Asymmetric Encryption (Public-Key Cryptography)**  
- Uses two keys:  
  - **Public Key** (encryption)  
  - **Private Key** (decryption)  
- Example: If encryption key = 5, decryption requires key = 21 (not the same).  

### **Symmetric Encryption**  
- Uses the **same key** for encryption & decryption.  

### **Hybrid Encryption**  
- Combines symmetric and asymmetric encryption for **secure bulk data transfer & digital signatures**.  

## **7. Public Key Infrastructure (PKI)**  
- **Client**: Requests secure communication.  
- **Server**: Provides proof of identity.  
- **Certificate Authority (CA)**: Issues certificates for authentication.  

## **8. RSA Encryption (Rivest-Shamir-Adleman)**  
- Uses mathematical properties of **prime numbers** to generate keys.  
### **Key Generation Steps**  
1. Select **two prime numbers** (P, Q).  
2. Compute **N = P × Q**.  
3. Compute **Totient**: (P-1) × (Q-1).  
4. Choose a **Public Key (E)**:  
   - Prime number  
   - Less than totient  
   - Not a factor of totient  
5. Compute **Private Key (D)**:  
   - \( D \times E \mod \) Totient = 1  

### **RSA Encryption & Decryption**  
- **Encryption**:  
  - Ciphertext = **Message^E mod N**  
- **Decryption**:  
  - Message = **Ciphertext^D mod N**  

## **9. Diffie-Hellman Key Exchange**  
- **Allows secure key exchange over an insecure network.**  
### **Process**  
1. Both parties choose a **prime number (P)** & **generator (G)**.  
2. Each generates a **private key (PK1, PK2)**.  
3. They compute and exchange **public keys** using:  
   - **(G^PK) mod P**  
4. Upon receiving the other's public key, they compute a **shared secret key**:  
   - **(Received PK)^Private Key mod P**  

## **10. Digital Signature Algorithm (DSA)**  
- **Ensures message authenticity but does NOT encrypt or exchange keys.**  
### **Operations**  
- **Signature Generation**: Uses **private key** & message.  
- **Signature Verification**: Uses **public key** & signature.  

## **11. Inspecting Certificates in Real-Time**  
- **Retrieve Certificate**:  
  ```bash
  openssl s_client -connect <site>:<port>
  ```  
- **Decrypt for Human-Readable Output**:  
  ```bash
  openssl x509 -in <certificate> -text -noout
  ```  

## **12. Certificate Extensions & Private Key Details**  
- Certificates may have **rules or restrictions** defining usage.  
- **Private Key Components**:  
  - **Modulus (N)** = P × Q  
  - **Public Exponent (E)** = Public Key  
  - **Private Exponent (D)** = Private Key  
  - **Prime 1 & 2 (P, Q)** = Used to generate N  
  - **Exponent 1 & 2, Coefficient** = Adds complexity for security  

### **Compare Certificate & Key Files**  
- **View Key File in Text**:  
  ```bash
  openssl rsa -in <keyfile.key> -noout -text
  ```  
- **Get Modulus of Certificate**:  
  ```bash
  openssl x509 -in <cert.cert> -noout -modulus
  ```  
- **Get Modulus of Key File**:  
  ```bash
  openssl rsa -in <keyfile.key> -noout -modulus
  ``` 
---
## **13. Certificate Signing Request (CSR)**
- Version : 0x0 = CSR ver.1
- DN : C= ST= L= O= OU= CN=
- Import DN certificate's issuer
- Public Key : Include Modulus and Exponent (Diff Structure)
- Attributes : 
	+ Extension Requests : requested for ensuring certificate
	+ Challenge Password : To controll administration
	+ a0:00 : if there are 0 attribute
---
## **14. File formats**
- DER (Distinguish Encoding Rules)
	+ Binary Encoded (Error if tried to extract content)
	+ Not for file exchanging
	+ File extensions : .der .cert .crt .csr

- PEM (Privacy Enhance Mail)
	+ Base64 Encoded version of DER format 
		- Every 6 bits is translate to a char
	+ Easy to copy/paste
	+ Contains : begin cert/privatekey/request and more
	+ File extensions : .pem .cert .crt .key .csr

- PKX / PKCS#12 (Personal Information Exchange/Public-key Cryptography Standard #12)
	+ Binary Encoded
	+ Contains : both public and private key in it
		- Chain certicate as well
	+ File extensions : .pfx .p12 .pkcs12

- PKCS#7 (Public-key Cryptography Standard#7)
	+ Base64 Encoded
	+ Sign : BEGIN PKCS7
	+ Contains : Certificate and/or Chains-only - no keys
	+ Not typically used for SSL and TLS
		- Originally used for S/MIME to share cert
			+ Secure Multipurpose internet mail extension
	+ File extensions : .pkcs7 .p7b .p7c
	
### Software formate
	+ java : DER
	+ Apach, linux, ASAs .. : PEM
	+ window, firefox ... : PFX, PKCS#12
	+ S/MIME, java/window : PKCS#7
---
## **14. Cert Validation**
+ Is it valid
	- Client use self private key to hash the content
	- Take x server certificate to if it the same
	- Then we can extract the content like expiration, url, name , revoked ...
	- Can be hash with 
		- RSA
		- DSA 
+ Is the ownder the real one
	- First Method 
		- client generate random value
		- client encrypt with server public key
		- server decrpyt with private key
		- value used to generate session keys
	- Seond Method
		- server generate "random" value (DH key)
		- server signs with server private key
		- client verifies with server public key
		- value used (indirect) to generate session keys