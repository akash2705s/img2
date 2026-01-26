import qrcode

def url_to_qr(url, filename="qr_code.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )

    # Add URL data
    qr.add_data(url)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save to file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
if __name__ == "__main__":
    url = "https://www.thepopcornfactory.com/"
    url_to_qr(url, "example_qr.png")
