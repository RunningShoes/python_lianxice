
from PIL import Image,ImageDraw


path1='1.jpeg'
path2='2.jpeg'
im1=Image.open(path1)
im2=Image.open(path2)
im2=im2.convert('RGB')
'''
直接转换会产生，rgba的第四个通道表示alpha，表示透明度
OSError: cannot write mode RGBA as JPE
OSError:无法将模式rgba作为jpeg写入
'''
weight1,height1=im1.size
weight2,height2=im2.size

print(weight1,height1)
print(weight2,height2)

im3 = im1.resize((1320, 700), Image.ANTIALIAS)  #最后一个参数表示平滑图片，高保真必备,抗锯齿   还有BILINEAR，BICUBIC
'''
图片 resize. size - 目标图像的尺寸，二元数组 (widthm height); resample - 重采样算法；Image.NEAREST(最近邻采样)，Image.BILINEAR(线性插值)，Image.BICUBIC(三次样条插值)，Image.LANCZOS(高质量下采样滤波器，high-quality downsampling filter). 当 resample=0，或者图片的 mode="1" 或 model="P" 时，默认采用 Image.NEAREST.
'''
im2.thumbnail((128, 128))   # 创建缩略图
im2.save('thumb.jpeg')
im3.show()
