import qrcode
img = qrcode.make("https://youtube.com")
img.save('myQR.jpg')