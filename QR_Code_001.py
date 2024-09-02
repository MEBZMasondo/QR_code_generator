import qrcode

# Data to encode
data = "Computer Science and Information Technology"

qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # about 7% or fewer errors can be corrected
    box_size=10,    # size of each box in pixels
    border=4,       # thickness of the border (minimum is 4)
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")
