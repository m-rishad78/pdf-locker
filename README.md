# 🔐 PDF Locker

 A Python based tool to **secure your PDF files** with a strong password. The program enforces password strength using the **zxcvbn** (https://github.com/dropbox/zxcvbn.git) library & creates a new locked PDF file, keeping your original file intact.

## 🚀 Features

 - Encrypt any PDF file with a password
 - Enforces strong passwords (zxcvbn score >= 3)
 - Keeps the original PDF safe; creates a new file with `_locked` suffix
 - Provides feedback for weak passwords
 - Handles exceptions & keyboard interrupts gracefully

## How it works

 - Generate a PDF writer object
 - Encrypt with the password
 - Save as `_locked.pdf`

## 📂 Project Structure

 ```tree
 📁 pdf-locker
 ├── .gitignore
 ├── main.py 
 ├── README.md
 └── requirements.txt
 ```

## 📦 Requirements

 - Python 3.8+
 - Dependencies:
    [`PyPDF2`]
    [`zxcvbn`]

## 1️⃣ Clone the Repository

 ```bash
 git clone https://github.com/m-rishad78/pdf-locker.git
 ```

## 2️⃣ Navigate to the Project Directory

 ```bash
 cd pdf-locker
 ```

## ⬇️ Install Dependencies

```bash
pip install -r requirements.txt
```

**or**

```bash
pip install PyPDF2 zxcvbn
```

## ▶️ Usage

 **01.** Run the program:

 ```bash
 python main.py
 ```

 **02.** Enter the PDF filename (must be in the same directory or provide the full path)  
 **03.** Enter a strong password  
 **04.** After successful encryption, a new PDF will be created with `_locked.pdf` suffix  


 Example:

 ```text
 Enter the PDF name: sample.pdf
 Enter the Password: ******

 [+] PDF Locked Successfully.
 ```
 
## 🧩 Code Structure

 - [`main.py`] main program containing the [`PDF`] class:
  - [`lock_file(filename, password)`] encrypts the PDF.
  - [`get_password()`] prompts for a strong password.
  - [`main`] runs the program.

## ⚠️ Security Note

 - The original PDF is **not overwritten**.
 - Password strength is enforced with zxcvbn.

## ⭐ Contributing

 Feel free to submit issues or pull requests.
 For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

 This project is open-source under the **MIT License.**
