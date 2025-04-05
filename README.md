# 🖼️ Image Steganography Decoder

This project demonstrates how to encode and decode secret messages inside images using basic steganography techniques in Python. It includes both a blue-channel embedding method and a green-channel differential decoding approach originally used to solve a professor's hidden message challenge.

---

## 🔍 What It Does

- ✅ Embed a message from a text file into the **blue channel** of an image
- ✅ Decode messages from the blue channel using ASCII interpretation
- ✅ Decode messages hidden using **green channel differences** between two images (professor challenge)

---

## 🧠 Technologies Used

- Python 3
- Pillow (PIL)
- ASCII encoding/decoding
- RGB image processing

---

## 🧪 Example Use Case

```python
write_secret_message_to_image("flowersColorFilm.png", "secretMessageFile.txt", "flowerMessage2.png")
read_secret_message("flowerMessage2.png")
decode_green_channel_difference("horseMessage.png", "horseRider3.png")
```

---

## 🐎 Professor's Hidden Message

Decoded using the green channel difference between `horseMessage.png` and `horseRider3.png`:

> "Congratulations. You have found the secret message. Make sure all your code passes all the tests and you have completely documented your work, including flowcharts and logic plans. Nicely done!"

---

## 📂 Folder Structure (Current)

```
Image_stenography/
├── flowerMessage2.png
├── flowersColorFilm.png
├── horseMessage.png
├── horseRider3.png
├── Image_steganography.py
├── secretMessageFile.txt
└── README.md
```

---

## 🏁 How to Run

1. Clone the repo:
```bash
git clone https://github.com/RaiknessDawn/Image-Steganography-Decoder.git
cd Image-Steganography-Decoder
```

2. Install Pillow:
```bash
pip install pillow
```

3. Run the project:
```bash
python Image_steganography.py
```

Make sure the image and message files are in the same folder as the script.

---

## 📦 Future Ideas

- Password-protect hidden messages
- Add Tkinter GUI for visual interaction
- Embed binary data instead of plain text
- Visual compare before/after images

---

## 👨‍💻 Author

Made with 🔍 pixels and 🧠 Python by Jason Acuna
