#!/usr/local/bin/python3#
#-*- coding: utf-8 -*-

import pillow as pil

# def add(im1,im2):
#     im1.ImageChops.invert(im1)
#     im3=ImageChops.darker(im1,im2)
#     im3.show()

def addNumber(im1):
    draw=ImageDraw.Draw(im1)
    draw.ellipse((530,10,630,110),fill='blue')
    # ft = ImageFont.truetype(60q)
    # font = ImageFont.truetype(fontsize=30)
    ft = ImageFont.truetype(r"/system/Library/Fonts/AquaKana.ttc",15)
    # draw.text((545,50),'Hwllo World!',fill='white')
    draw.text((545,50),'Hello World!',font=ft)

from PIL import Image,ImageChops,ImageDraw,ImageFont

im1=Image.open('1.jpeg')
im2=Image.open('2.jpeg')

w,h=im1.size
print(w,h)

# r,g,b = im1.split()
# im1 = Image.merge('RGB',(b,g,r))
addNumber(im1)
im1.show()
# im2.show()

