# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:09:41 2022
qr code genrator
@author: sudhanshu vidyrthi
"""
import qrcode
import image
qr=qrcode.QRCode(
        version= 15,
        box_size= 10,
        border=5
        )
#we can remove that data also
data= input("this is qr data wanna enter anything ")
qr.add_data(data)
qr.make(fit=(True) )
img=qr.make_image(fill ="black",black_color="white")
qrr=img.save("test.png")
print("qrr")
