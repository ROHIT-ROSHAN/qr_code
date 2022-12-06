import qrcode as qr


#provide link of the site to generate qr code
img=qr.make("https://www.linkedin.com/in/rohit-roshan-4b8a35b8")

#saving the qrcode as an image
img.save("linkedin-profile.png")

