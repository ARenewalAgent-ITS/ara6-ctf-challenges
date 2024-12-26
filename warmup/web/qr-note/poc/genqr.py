import qrcode

data = input("QR Content: ")
img = qrcode.make(data)

img.save("qr.png")