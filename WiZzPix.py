from PIL import Image  # Import the Image module from the Python Imaging Library (PIL)
import pyfiglet
import colorama
from colorama import Fore

# Initialize colorama for colored output
colorama.init(autoreset=True)

def display_name():
    """
    Display the name "WiZzPix" using figlet.
    """
    # Generating  ASCII art of "WiZzPix" using the figlet library
    
    path1 = "figlet-fonts/Graffiti"
    path2 = "figlet-fonts/wideterm"

    ascii_art1 = pyfiglet.figlet_format("WiZzPix", font=path1, justify = "center")
    ascii_art2 = pyfiglet.figlet_format("Ethical WiZzzrd", font=path2, justify="center")

    # Printing the ASCII art in blue color for better visibility
    print(Fore.YELLOW + ascii_art1)
    print(ascii_art2)

# Function to encrypt an image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size  # Get the width and height of the image
    
    # Encrypt the image pixel by pixel using XOR operation with the key
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))  # Get the pixel value at coordinates (x, y)
            encrypted_pixel = tuple((p ^ key) for p in pixel)  # XOR operation with the encryption key
            encrypted_pixels.append(encrypted_pixel)  # Append the encrypted pixel to the list
    
    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)  # Create a new image with the same mode and size
    encrypted_img.putdata(encrypted_pixels)  # Put the encrypted pixel data into the new image
    
    return encrypted_img  # Return the encrypted image

# Function to decrypt an image
def decrypt_image(encrypted_img, key):
    width, height = encrypted_img.size  # Get the width and height of the encrypted image
    
    # Decrypt the image pixel by pixel using XOR operation with the key
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))  # Get the pixel value at coordinates (x, y)
            decrypted_pixel = tuple((p ^ key) for p in pixel)  # XOR operation with the decryption key
            decrypted_pixels.append(decrypted_pixel)  # Append the decrypted pixel to the list
    
    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)  # Create a new image with the same mode and size
    decrypted_img.putdata(decrypted_pixels)  # Put the decrypted pixel data into the new image
    
    return decrypted_img  # Return the decrypted image

display_name()
# Input encryption key and image path from the user
key = int(input("Enter encryption key: "))  # Prompt the user to enter the encryption key
image_path = input("Enter image path: ")  # Prompt the user to enter the path to the image

# Menu system for the user to choose encryption, decryption, or exit
while True:
    print("\nMenu:")
    print(Fore.BLUE + "1. Encrypt Image")
    print(Fore.GREEN + "2. Decrypt Image")
    print(Fore.RED + "3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")  # Prompt the user to enter a choice

    if choice == '1':
        # Encrypt the image
        encrypted_image = encrypt_image(image_path, key)  # Call the encrypt_image function
        encrypted_image.save("encrypted_image.png")  # Save the encrypted image to a file
        print("Image encrypted successfully!")  # Print a success message
    elif choice == '2':
        # Decrypt the encrypted image
        encrypted_image_path = input("Enter path to the encrypted image: ")  # Prompt the user to enter the path to the encrypted image
        encrypted_image = Image.open(encrypted_image_path)  # Open the encrypted image
        decrypted_image = decrypt_image(encrypted_image, key) # Call the decrypt_image function
        decrypted_image.save("decryped_image.png") # Save decrypted image to a file
        decrypted_image.show()  # Display the decrypted image
    elif choice == '3':
        print("Exiting the program.")  # Print a message indicating program exit
        break  # Exit the while loop and terminate the program
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")  # Print an error message for invalid choice

