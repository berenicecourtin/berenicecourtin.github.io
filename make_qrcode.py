import qrcode
import os

os.makedirs("QRcode", exist_ok=True)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://www.berenicecourtin.com/project-b.html")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QRcode/qr_codeproject-b.png")

print("Saved: QRcode/qr_codeproject-b.png")

