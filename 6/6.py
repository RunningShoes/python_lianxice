
from PIL import Image,ImageDraw

path='1.jpeg'
im1=Image.open(path)
im2=Image.open('2.jpeg')
weight1,height1=im1.size
weight2,height2=im2.size

print(weight1,height1)
print(weight2,height2)

im3 = im1.resize((1320, 700), Image.ANTIALIAS)  #最后一个参数表示平滑图片，高保真必备,抗锯齿
im3.show()
