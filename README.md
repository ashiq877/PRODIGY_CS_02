Here’s a README file for the updated Image Encryption and Decryption Tool that includes instructions, features, and usage:

---

# Image Encryption and Decryption Tool

## Overview
This Python program implements an image encryption and decryption tool using a simple noise-based method. The program allows users to encrypt an image by applying a random noise factor and decrypt it back to its original form. It utilizes the `PIL` (Pillow) library for image processing and `numpy` for numerical operations.

## Features
- **Encrypt Images**: Encrypt an image by applying a noise-based transformation.
- **Decrypt Images**: Decrypt the previously encrypted image back to its original form.
- **Reset Functionality**: Reset the encryption state of the image.
- **Supports Grayscale Images**: The program processes images in grayscale format.

## Requirements
- Python 3.x
- `numpy` library
- `Pillow` library (PIL)

### Installation
You can install the required libraries using pip:
```bash
pip install numpy Pillow
```

## Usage
1. Clone or download the script to your local machine.
2. Run the program using Python:
    ```bash
    python image_encryption.py
    ```
3. Follow the prompts to:
    - Encrypt an image by providing its path.
    - Decrypt an image if you have encrypted one.
    - Reset the image state if needed.
4. Make sure to provide the file path in the format without the `file://` prefix (e.g., `/home/tony/Downloads/ashiq.png`).

### Example
```bash
Image Encryption and Decryption Tool
1. Encrypt Image
2. Decrypt Image
3. Reset Image
4. Exit
Choose an option (1-4): 1
Enter the path of the image to encrypt: /home/tony/Downloads/ashiq.png
Image encrypted successfully and saved as 'image_encrypted.jpg'.
```

## Functions

### `get_file_path(prompt)`
Prompts the user to enter a file path and strips any unnecessary prefixes (like `file://`).

### `encrypt_image(input_path)`
Encrypts the image at the specified `input_path` by applying a noise-based transformation and saves the encrypted image.

### `decrypt_image()`
Decrypts the previously encrypted image and saves it as `image_output.jpg`.

### `reset_image(original_path)`
Resets the encryption state of the image.

### `main()`
Handles the user interface and options for encryption, decryption, and resetting images.

## Notes
- Ensure that the image paths are correct and that the images exist at those locations.
- The program currently supports only grayscale images; color images will be converted to grayscale upon encryption.
- The encrypted image is saved as `image_encrypted.jpg`, and the decrypted image is saved as `image_output.jpg`.

## License
This program is open source. Feel free to modify, use, and distribute it.

---

You can customize the README further to match your style or add additional sections as needed!
