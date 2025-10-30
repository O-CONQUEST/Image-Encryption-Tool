from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Encrypt by adding the key to each pixel value (mod 256)
    encrypted_pixels = (pixels + key) % 256
    
    encrypted_image = Image.fromarray(np.uint8(encrypted_pixels))
    encrypted_image.save(output_path)
    print(f"✅ Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Decrypt by subtracting the key (mod 256)
    decrypted_pixels = (pixels - key) % 256
    
    decrypted_image = Image.fromarray(np.uint8(decrypted_pixels))
    decrypted_image.save(output_path)
    print(f"🔓 Image decrypted and saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    input_path = input("Enter the path of the image: ")
    output_path = input("Enter the output file name (with .png or .jpg): ")
    key = int(input("Enter encryption key (1-255): "))
    
    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
