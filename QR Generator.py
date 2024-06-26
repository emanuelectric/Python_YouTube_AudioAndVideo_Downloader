import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from PIL import Image, ImageOps
import tkinter as tk
from tkinter import messagebox


def generate_qr():
    link = entry_link.get()
    title = entry_title.get()

    if not link or not title:
        messagebox.showwarning("Input Error", "Both fields must be filled.")
        return

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(link)
    img = qr.make_image(
        image_factory=StyledPilImage, module_drawer=CircleModuleDrawer()
    )

    # Convert to inverted colors
    img = img.convert("RGB")  # Convert to RGB mode
    inverted_img = ImageOps.invert(img)

    file_path = f"{title}.jpeg"
    inverted_img.save(file_path)
    messagebox.showinfo("Success", f"QR Code saved as {file_path}")

    # Clear the input fields
    entry_link.delete(0, tk.END)
    entry_title.delete(0, tk.END)


# Create the GUI
root = tk.Tk()
root.title("QR Code Generator")

# Link input
tk.Label(root, text="Enter Link:").grid(row=0, column=0, padx=10, pady=10)
entry_link = tk.Entry(root, width=50)
entry_link.grid(row=0, column=1, padx=10, pady=10)

# Title input
tk.Label(root, text="Enter Title:").grid(row=1, column=0, padx=10, pady=10)
entry_title = tk.Entry(root, width=50)
entry_title.grid(row=1, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
