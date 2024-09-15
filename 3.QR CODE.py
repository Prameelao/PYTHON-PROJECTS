###qr code python
##import qrcode as qr
##img=qrcode.make("https://in.search.yahoo.com/search?fr=mcafee&type=E211IN885G0&p=youtube.com")
##img.save("YOUTUBE.png")


import qrcode

# Create a QR code instance with default settings
qr = qrcode.make('https://www.example.com')

# Save the QR code image
qr.save('example_qr.png')
