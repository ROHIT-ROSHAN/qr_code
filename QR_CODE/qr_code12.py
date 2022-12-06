import qrcode

from PIL import Image


qr=qrcode.QRCode(version=1,

                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
                )

qr.add_data("https://www.linkedin.com/in/rohit-roshan-4b8a35b8")
qr.make(fit=True)

#changing the color
img=qr.make_image(fill_color="red",back_color="white")

#saving the image
img.save("my-linkedin-profile.png")