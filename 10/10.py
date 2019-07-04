#!usr/local/bin/python3
# -*-coding:utf-8 -*-


import random
from PIL import ImageFont,ImageDraw,Image,ImageFilter


def rndChar():
    return (chr(random.randint(65,90)))

def randomColor():
    return (random.randint(32,255),random.randint(32,255),random.randint(32,255))

def randomColor2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))


height=60
width=60*4
image=Image.new('RGB',(width,height),(255,255,255))
font1=ImageFont.truetype(r'/system/Library/Fonts/Arial.ttf',36)
draw=ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randomColor())

for ch in range(4):
    draw.text((60 * ch+10,10),rndChar(),font=font1,fill=randomColor())
    # draw.text((60*ch+10,10),charColor(), font=font1, fill=randomColor())

image=image.filter(ImageFilter.BLUR)
image.show()
