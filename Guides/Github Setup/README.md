___
# Setting up Github on PC
![welcome](https://imgs.search.brave.com/pW-GGWmPHHzukduHH8U3udwJUEIvDLz2zcxPFZvmbG0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS50ZW5vci5jb20v/eGoweGh5OWJCZ0FB/QUFBai9tZW1lZmFj/ZS5naWY.jpeg)
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
```bashd
ssh -T git@github.com
```
### 6. Create a GitHub repository
___
![pullup](https://imgs.search.brave.com/nL9Q1DRLe0TB8vyjWh8R4XX2EU3PB5dD2Zi331t1Qrw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmt5/bS1jZG4uY29tL3Bo/b3Rvcy9pbWFnZXMv/bGlzdC8wMDIvOTk5/LzM0NS9mZDEuZ2lm.gif)
___

# Push and Pull
### 1. Create Folder 
### 2. Initialize local repository :
```bash
git init
```
### 3. Add & Commit files
+ Add files
```bash
git add .
```
+ Commit changes
```bash
git commit -m "<Enter Message>"
```
### 4. Connect GitHub :
```bash
git remote add origin <repo-url>
```
### 5. Push changes to GitHub :
```bash
git push -u origin main
```
### 6. `Repeat the Process if you changed something`
### 7. Pull updates from GitHub :
```bash
git pull origin main
```
___
![clone](https://imgs.search.brave.com/mckGpb-5mSmNz4fs_N9cM6gI_vfO0Lty7pnLVUnQGy4/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS50ZW5vci5jb20v/T2ZUZ3lrbWktVFVB/QUFBTS9zaGFkb3ct/Y2xvbmUtY2xvbmUu/Z2lm.jpeg)
___

#  Cloning and Working with Repositories
### 1. Clone an existing repository :
```bash 
git clone <repo-url>
```
### 2. `Make changes, commit, and push`
### 3. Create and switch branches :
```bash
git branch feature-branch
```
```bash
git checkout feature-branch
```
### 4. Merge branches :
```bash
git merge feature-branch
```
### 5. `Resolve merge conflicts`
### 6. Delete branches :
```bash
git branch -d feature-branch
```
