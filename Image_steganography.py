
# all import statements

from PIL import Image


def write_secret_message_to_image(img_to_open, text_file, image_to_save):
    """
    Embeds a secret message from a text file into the blue channel of an image.

    Each character of the text is converted to its ASCII value and stored in the blue
    channel of each pixel. Remaining pixels (if any) are filled with space characters (ASCII 32).

    :param img_to_open: Path to the source image file.
    :type img_to_open: str
    :param text_file: Path to the text file containing the message to hide.
    :type text_file: str
    :param image_to_save: Path where the modified image will be saved.
    :type image_to_save: str
    :return: None. Saves the encoded image to disk.
    :rtype: None
    """
    try:
        img = Image.open(img_to_open)
        pixel_map = img.load()

        # Read the text file and convert it into ASCII values
        with open(text_file, "r", encoding="utf-8") as file:
            list_of_chars = [
                ord(char)
                for char in " ".join(file.readlines()).replace("\n", " ")
            ]
        message_cnt = 0
        for i in range(img.size[0]):  # Use img.size directly
            for j in range(img.size[1]):
                t_one, t_two, t_three = img.getpixel(
                    (i, j)
                )[:3]  # Extract RGB values
                t_three = (
                    list_of_chars[message_cnt]
                    if message_cnt < len(list_of_chars)
                    else 32
                )
                pixel_map[i, j] = (t_one, t_two, t_three)
                message_cnt += 1

        img.save(image_to_save, format="PNG")  # Save modified image
    except IOError as e:
        print(f"Error occurred: {e}")


def read_secret_message(image_to_open):
    """
    Decodes a hidden message from the blue channel of an image.

    Reads each pixel’s blue channel value and converts it to a character if it falls
    within the printable ASCII range (32–126). Reconstructs the message and prints it.

    :param image_to_open: Path to the image containing the hidden message.
    :type image_to_open: str
    :return: None. The decoded message is printed to the console.
    :rtype: None
    """
    try:
        img = Image.open(image_to_open)
        width, height = img.size
        pixel_map = img.load()

        list_of_chars = []
        for i in range(width):
            for j in range(height):
                t_three = pixel_map[i, j][2]  # Extract blue channel
                if 31 < t_three < 127:  # Keep valid ASCII characters only
                    list_of_chars.append(t_three)

        decoded_message = ""
        num_of_spaces = 0

        # Decode the characters
        for char_val in list_of_chars:
            if char_val == 32:  # ASCII space
                num_of_spaces += 1
            else:
                num_of_spaces = 0
            decoded_message += chr(char_val)
            if num_of_spaces > 80:  # Stop decoding after excessive spaces
                break

        print("Decoded message:", decoded_message.strip())  # Cleaner output
    except IOError as e:
        print(f"Error occurred: {e}")


def decode_green_channel_difference(image_to_open, orig_image):
    """
    Decodes a secret message hidden in the green channel difference between two images.

    This function was used to solve a steganography challenge from my professor.
    It compares the green value of each pixel in the modified image to the original image,
    interprets the differences as ASCII characters, and reconstructs the hidden message.

    :param image_to_open: Path to the image containing the hidden message.
    :type image_to_open: str
    :param orig_image: Path to the original image used for comparison.
    :type orig_image: str
    :return: None. The decoded message is printed to the console.
    :rtype: None
    """
    try:
        # Open both images
        img = Image.open(image_to_open)
        org_img = Image.open(orig_image)

        # Make sure both images are the same size before we compare them
        if img.size != org_img.size:
            print("Error: Image sizes do not match!")
            return
        # Load pixel data from both images
        pixel_map = img.load()
        org_map = org_img.load()
        list_of_chars = []  # This will store the extracted message
        # Check if the image is RGB (3 channels) or
        # RGBA (4 channels)
        img_mode = img.mode  # Either 'RGB' or 'RGBA'

        for i in range(img.size[0]):
            # Loop through width
            for j in range(img.size[1]):
                # Loop through height
                if img_mode == "RGBA":
                    # Get the green channel from both images
                    _, t_two, _, _ = pixel_map[i, j]
                    # Green from encoded image
                    _, orig_t_two, _, _ = org_map[i, j]
                    # Green from original
                else:  # RGB image (no transparency)
                    _, t_two, _ = pixel_map[i, j]
                    _, orig_t_two, _ = org_map[i, j]

                # The hidden message is stored as
                # the difference in green values
                char_value = t_two - orig_t_two

                # Only add valid ASCII characters to
                # the message
                if 32 <= char_value <= 126:
                    list_of_chars.append(chr(char_value))
        # Join all characters into a single string
        decoded_message = "".join(list_of_chars)
        print("Decoded complex message:", decoded_message.strip())

    except IOError as e:
        # If the file can't be opened, let the user know
        print(f"Error: Unable to open file - {e}")
    except ValueError as e:
        # Handle any unexpected numerical errors
        print(f"Value error encountered: {e}")


def main():
    """
    Demonstrates basic and complex steganography techniques using image files.

    Encodes a message into the blue channel of one image, reads it back, and also
    decodes a separate message hidden in the green channel differences of two images.

    :return: None
    :rtype: None
    """
    # img  = Image.open(path)
    # On successful execution of this statement,
    # an object of Image type is returned and stored in img variable
    # t_one = red
    # t_two = green
    # t_three = blue

    # Embed a secret message into an image by modifying the blue channel
    write_secret_message_to_image('flowersColorFilm.png',
                                  "secretMessageFile.txt",
                                  "flowerMessage2.png")

    # Retrieve the hidden message from the encoded image
    read_secret_message("flowerMessage2.png")

    # Extract a complex hidden message stored in the green channel
    decode_green_channel_difference('horseMessage.png',
                                    'horseRider3.png')


# main function call
if __name__ == '__main__':
    main()
