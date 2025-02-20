# Setting up Github on PC

### 1. [Download & install Git](https://git-scm.com/)
### 2. Verify installation :
```bash
git --version
```
### 3. Set up Git :
+ Username
    ```bash
    git config --global user.name <Username>
    ```
+ Email
    ```bash
    git config --global user.email <Email@example.com>
    ```
### 4. Generate/add SSH keys for authentication :
```bash
ssh-keygen -trsa -b 4096
```
### 5. Test Connection 
```bash
ssh -T git@github.com
```
### 6. Create a GitHub repository