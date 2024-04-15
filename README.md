# PRODIGY_CS_02

# WiZzPix

WiZzPix is a basic image encryption and decryption tool developed as part of my internship project to explore Python programming for creating cybersecurity-related tools.

## Overview

This Python script allows users to encrypt and decrypt images using a simple XOR encryption algorithm. Let's explore its functionality:

### Importing Libraries

The script imports the PIL (Python Imaging Library) for image manipulation, pyfiglet for generating ASCII art, and colorama for colored output. `colorama.init(autoreset=True)` is used to automatically reset color settings after each print statement.

### Displaying Name

The `display_name()` function generates ASCII art for the name "WiZzPix" using pyfiglet and prints it in yellow color.

### Image Encryption and Decryption Functions

- **Encrypt Function**: The `encrypt_image()` function encrypts images pixel by pixel using XOR operation with a user-defined encryption key.
- **Decrypt Function**: The `decrypt_image()` function decrypts encrypted images back to their original form using the same encryption key.

### Main Function

The main functionality of the script is wrapped within a user-friendly menu system:
- Users are prompted to choose between encrypting an image, decrypting an image, or exiting the program.
- Depending on the choice, users are prompted for input such as encryption key and image path, and the appropriate function is called to perform the desired operation.

### Execution

The script can be executed by running the `WiZzPix.py` file. It provides a simple command-line interface for users to interact with.

## Usage

### Steps to Run the Tool

1. Clone the repository:
   ```
   git clone https://github.com/Krishardik/PRODIGY_CS_01
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Navigate to the project directory:
   ```
   cd PRODIGY_CS_02
   ```

4. Run the script:
   ```
   python WiZzPix.py
   ```

## Note

- Ensure to keep your encryption keys secure and share them only with authorized users.
- Use this tool responsibly and ethically in compliance with applicable laws and regulations.
