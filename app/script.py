from PIL import Image, ImageEnhance, ImageFilter
from configparser import SafeConfigParser
import os
import shutil

path = '/home/willian/Downloads/imagem.asp.gif'
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 0)
img.save('/home/willian/Desktop/tesserpython/images/temp1.png')
os.rename(path, "/home/willian/NetBeansProjects/imagem.asp.gif")
shutil.move(path, "/home/willian/NetBeansProjects/xlsdwnloadanp/dephbycapcha/imagem.asp.gif")
print("success generated image")
