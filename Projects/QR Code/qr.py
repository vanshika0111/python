# pip install qrcode

import qrcode

data = 'This QR code is created by Vanshika'

# -------------------------------- Simple QR Code ---------------------------------------
# image = qrcode.make(data)
# image.save('C:/Users/VANSHIKA/Desktop/coding_world/python/Projects/QR Code/myqr.png')

# --------------------------------- Format QR Code ---------------------------------------
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='blue', back_color='white')
image.save(
    'C:/Users/VANSHIKA/Desktop/coding_world/python/Projects/QR Code/myqr.png')
a = input("Enjoyed:")
