# Image Encryption Tool 🔒  
**Prodigy InfoTech Cybersecurity Internship – Task 02**

This project is a simple **image encryption and decryption tool** built using Python.  
It uses pixel manipulation to secure images by applying a basic mathematical operation to each pixel.  

---

##  Features
- Encrypt any image using a user-defined key  
- Decrypt the encrypted image using the same key  
- Simple CLI interface (no extra setup needed)  

---

##  How It Works
The program reads image pixels using **Pillow** and converts them into arrays using **NumPy**.  
Each pixel’s RGB value is modified using the encryption key:
EncryptedPixel = (OriginalPixel + key) % 256
To decrypt, the same key is subtracted:
DecryptedPixel = (EncryptedPixel - key) % 256

---

## 🧰 Technologies Used
- Python  
- Pillow (PIL)  
- NumPy  

---

## 🏃‍♂️ How to Run
1. Clone this repository:
   git clone https://github.com/yourusername/Image-Encryption-Tool.git

2. Install dependencies:
    python -m pip install pillow numpy

3. Run the program
   python image_encryption.py

   
