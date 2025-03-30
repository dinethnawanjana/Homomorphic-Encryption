# Homomorphic Encryption Demonstrator 🔐

## Overview 🚀
This is a simple GUI-based application that demonstrates **Homomorphic Encryption** using **ElGamal-like encryption**. The app is built with **Tkinter (Python)** and allows users to perform encryption, homomorphic addition, and decryption of numerical values.

## Features ✨
- **Initialize Encryption System** with user-defined prime number (p) and generator (g).
- **Encrypt Messages** using ElGamal-like encryption.
- **Perform Homomorphic Addition** on two encrypted messages.
- **Decrypt Results** after homomorphic operations.

## Technologies Used 🛠️
- **Python** 🐍
- **Tkinter** (for GUI) 🎨
- **Random, Math Libraries** (for cryptographic calculations) 🔢

## Installation & Setup ⚙️
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/homomorphic-encryption-app.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd homomorphic-encryption-app
   ```
3. **Install dependencies**
   ```bash
   # First, install tkinter (it's usually built-in with Python)
   python -m pip install --upgrade pip

   # Install packages
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python main.py
   ```

## How It Works? 🤔
1. **Initialize the encryption system** by providing a prime number (p) and a generator (g).
2. **Encrypt two messages** and store their ciphertexts.
3. **Perform Homomorphic Addition**, which results in an encrypted sum.
4. **Decrypt the result** to retrieve the sum of the original numbers.

## Example Usage 📝
```
Prime Number (p): 17
Generator (g): 3
Message 1: 5
Message 2: 7

[Encrypt Messages]
Ciphertext 1: (c1, c2)
Ciphertext 2: (c1, c2)

[Perform Homomorphic Addition]
Encrypted Sum: (c1, c2)

[Decrypt]
Decrypted Sum: 12
```

## Screenshots 🖼️
| SCREEN | SCREEN | 
|---------|------------|
| ![H-1](https://github.com/user-attachments/assets/036f26ac-ad88-45d2-ac31-53a3377d1f14) | ![H-2](https://github.com/user-attachments/assets/11b3ff7c-6c2b-4d42-a05a-3be3c075fcdc) |
| ![H-3](https://github.com/user-attachments/assets/77711ca6-b1f6-421d-aef5-dc68d7688e1d) | ![H-4](https://github.com/user-attachments/assets/493b6c29-66dd-4878-82f3-114185b836cb) |
| ![h-5](https://github.com/user-attachments/assets/35a9a069-633b-4451-a3bf-5d00f56b48bc) | ![h-6](https://github.com/user-attachments/assets/ea2ff514-f076-4206-a545-2b49798117a8) |
| ![h-7](https://github.com/user-attachments/assets/2117d3fd-ef0d-4c0a-a1f3-6d5c1a9e0b3a) | ![h-8](https://github.com/user-attachments/assets/c232d831-f13d-441d-9504-207e40781343) |
