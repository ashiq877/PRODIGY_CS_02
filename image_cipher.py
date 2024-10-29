import os
import numpy as np
from PIL import Image

image_encrypted = None
key = None

def get_file_path(prompt):
    return input(prompt)

def encrypt_image(input_path):
    global image_encrypted, key
    try:
        # Read image in grayscale
        image_input = Image.open(input_path).convert('L')
        image_input_np = np.array(image_input) / 255.0  # Normalize to [0, 1]
        
        (x1, y) = image_input_np.shape
        mu, sigma = 0, 0.1
        key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps  # Generate noise
        image_encrypted = image_input_np / key  # Encrypt image
        
        # Save encrypted image
        encrypted_file = 'image_encrypted.jpg'
        encrypted_image = Image.fromarray((image_encrypted * 255).astype(np.uint8))  # Convert back to image format
        encrypted_image.save(encrypted_file)
        print(f"Image encrypted successfully and saved as '{encrypted_file}'.")
    except Exception as e:
        print("Failed to read the image:", e)

def decrypt_image():
    global image_encrypted, key
    if image_encrypted is not None and key is not None:
        image_output = image_encrypted * key
        image_output *= 255.0
        
        # Save decrypted image
        decrypted_file = 'image_output.jpg'
        decrypted_image = Image.fromarray(image_output.astype(np.uint8))  # Convert back to image format
        decrypted_image.save(decrypted_file)
        print(f"Image decrypted successfully and saved as '{decrypted_file}'.")
    else:
        print("No image has been encrypted yet.")

def reset_image(original_path):
    global image_encrypted
    image_encrypted = None
    print("Image reset to original format.")

def main():
    global image_encrypted
    while True:
        print("\nImage Encryption and Decryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Reset Image")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            input_path = get_file_path("Enter the path of the image to encrypt: ")
            encrypt_image(input_path)

        elif choice == '2':
            decrypt_image()

        elif choice == '3':
            original_path = get_file_path("Enter the path of the original image to reset: ")
            reset_image(original_path)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
