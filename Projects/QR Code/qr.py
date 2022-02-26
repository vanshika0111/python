# pip install qrcode

import qrcode

data = 'This QR code is created by Vanshika'

image = qrcode.make(data)

image.save('C:/Users/VANSHIKA/Desktop/coding_world/python/Projects/QR Code/myqr.png')