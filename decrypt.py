import cv2

def decrypt_image(encrypted_image="encryptedImage.png"):
    img = cv2.imread(encrypted_image)
    if img is None:
        print("Error: Encrypted image not found.")
        input("Press Enter to exit...")
        return

    # Load stored password
    try:
        with open("password.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Password file not found!")
        input("Press Enter to exit...")
        return

    pas = input("Enter passcode for Decryption: ")
    if pas != stored_password:
        print("YOU ARE NOT AUTHORIZED")
        input("Press Enter to exit...")
        return

    c = {i: chr(i) for i in range(256)}

    n, m, z = 0, 0, 0

    # Retrieve message length safely using bitwise operations
    message_length = img[n, m, z]  # Lower 8 bits
    n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3
    message_length |= img[n, m, z] << 8  # Higher 8 bits

    message = ""

    # Decode the message
    for _ in range(message_length):
        n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3
        message += c[img[n, m, z]]

    print("Decryption message:", message)

    input("Press Enter to exit...")  # Prevents window from closing

if __name__ == "__main__":
    decrypt_image()
