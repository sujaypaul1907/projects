#QR code generator

import qrcode as qr

x = input("Enter URL or text to make its QR code: ")
y = input("Enter QR code name: ")

img = qr.make(x)
img.save(f"{y}.png")

print("QR code generated succesfully")
