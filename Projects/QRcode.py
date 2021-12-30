import qrcode

image = qrcode.make('https://github.com/yoge-esh')
image.save('qr.png')