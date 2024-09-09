import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator - Modern UI")
        self.root.geometry("400x500")
        self.root.config(bg="#1e1e1e")

        # Label for text/URL input
        self.label = tk.Label(root, text="Enter text or URL:", bg="#1e1e1e", fg="white", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        # Entry for user input
        self.entry = tk.Entry(root, width=30, font=("Arial", 14), relief="flat", bg="#2e2e2e", fg="white")
        self.entry.pack(pady=10)

        # Button to generate the QR code
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr, bg="#3498db", fg="white", font=("Arial", 14), relief="flat")
        self.generate_button.pack(pady=20)

        # Label to display the generated QR code
        self.qr_label = tk.Label(root, bg="#1e1e1e")
        self.qr_label.pack(pady=20)

        # Button to save the generated QR code
        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr, bg="#2ecc71", fg="white", font=("Arial", 14), relief="flat")
        self.save_button.pack(pady=10)

        # Variable to store the QR image
        self.qr_image = None

    def generate_qr(self):
        # Get the input data from the user
        data = self.entry.get()
        if data:
            # Generate QR code
            qr_code = qrcode.make(data)

            # Convert image to displayable format in Tkinter
            self.qr_image = ImageTk.PhotoImage(qr_code.resize((200, 200)))
            self.qr_label.config(image=self.qr_image)

    def save_qr(self):
        if self.qr_image:
            # Save the QR code as an image
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                qr_code = qrcode.make(self.entry.get())
                qr_code.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
