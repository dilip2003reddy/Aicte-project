import cv2
import os

def encrypt_image(message, password, input_image="mypic.jpg", output_image="encryptedImage.png"):
    img = cv2.imread(input_image)
    if img is None:
        print("Error: Image not found.")
        return

    message_length = len(message)
    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0

    # Store message length in first two pixels
    img[n, m, z] = message_length % 256
    n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3
    img[n, m, z] = message_length // 256

    # Encode message into pixels
    for char in message:
        n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3
        img[n, m, z] = d[char]

    # Save encrypted image
    cv2.imwrite(output_image, img)
    print(f"Message encrypted and saved as {output_image}")

    # Store password
    with open("password.txt", "w") as f:
        f.write(password)

    os.system(f"start {output_image}")  # Open the image on Windows

if __name__ == "__main__":
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(message, password)
