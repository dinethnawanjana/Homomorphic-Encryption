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
| ![H-1](https://github.com/user-attachments/assets/19767ca5-4c59-4cce-8f6f-51246ae06c4c) | ![H-2](https://github.com/user-attachments/assets/0c06735c-ed23-41de-8af5-c15f26d79d9c) |
| ![H-3](https://github.com/user-attachments/assets/780b56f9-283a-4237-ac6f-d8491e398bbc) | ![H-4](https://github.com/user-attachments/assets/2df97573-35b6-42e4-b85b-cb8ecbc1dbb6) |
| ![h-1](https://github.com/user-attachments/assets/6233063e-4dd4-4e6d-81f6-5fca620903cd) | ![h-2](https://github.com/user-attachments/assets/9e2b1a5a-1b5d-4536-b4ce-ea13d8188205) |
| ![h-3](https://github.com/user-attachments/assets/8cd30962-f0fc-4aaf-a0d8-2bc993f375d9) | ![h-4](https://github.com/user-attachments/assets/47b65c44-c2b9-41b9-8e59-59234c3a6092) |
|![h-5](https://github.com/user-attachments/assets/6a0b0dbe-a56c-4f53-9283-84be6c963343) | ![h-6](https://github.com/user-attachments/assets/9729a1b0-0271-494a-a87e-4353cad0f008) |
| ![h-7](https://github.com/user-attachments/assets/83d1a010-2663-47d1-a023-0c8b093ff388) | ![h-8](https://github.com/user-attachments/assets/c3376b90-4e4a-4fa8-873d-6ad0feceaf9b) |

# Homomorphic Encryption Demonstrator

## Overview
A desktop application demonstrating the principles of homomorphic encryption with a user-friendly interface.

## Features
- Initialize custom encryption parameters
- Encrypt multiple messages
- Perform homomorphic addition
- Decrypt results

## Requirements
- Python 3.7+
- Tkinter (comes standard with Python)

## Installation
1. Clone the repository
2. Ensure Python 3.7+ is installed
3. Run `python main.py`

## Usage
1. Set Prime (p) and Generator (g)
2. Click "Initialize Encryption"
3. Encrypt two messages
4. Perform homomorphic addition
5. Decrypt the result

## Project Structure
- `main.py`: Application entry point
- `core/`: Encryption logic
- `ui/`: User interface components

## Learning Objectives
- Understand homomorphic encryption principles
- Visualize encryption/decryption process
- Explore computational capabilities of encrypted data

## Project Structure 📂
```
homomorphic_encryption_app/
│
├── main.py - Application entry point
├── config.py - Configuration settings
│
├── core/
│   ├── __init__.py
│   ├── encryption.py - Core encryption logic
│   ├── text_encryption.py - Text-based encryption logic
│   └── utils.py - Utility functions for cryptographic operations
│
├── ui/
│   ├── __init__.py
│   ├── app.py - Main GUI application
│   ├── dashboard.py - Dashboard interface
│   ├── encryption_page.py - Encryption UI
│   ├── operations_page.py - Operations UI
│   ├── results_page.py - Results display UI
│   └── visualization.py - Data visualization components
│
├── utils/
│   ├── __init__.py
│   ├── converters.py - Data conversion utilities
│   └── validators.py - Input validation utilities
│
├── static/
│   ├── icons/ - Application icons
│   └── styles/ - CSS and UI styles
│
├── requirements.txt - Required dependencies
└── README.md - Documentation
```

## Contribution 🤝
Feel free to **fork** this repository and submit **pull requests** to improve the application! 

## License 📜
This project is licensed under the MIT License. See the [LICENSE](https://codeshow-lapz.web.app) file for details.
