import qrcode
image = qrcode.make('https://docs.python.org/3/py-modindex.html')
image.save('qr.png')