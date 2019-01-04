from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = '/home/willian/Desktop/selenium/capch-free.gif'
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save('temp1.png')
im = Image.open("temp1.png")
text1 = pytesseract.image_to_string(Image.open('temp1.png'))
print(text1)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.png')
text = pytesseract.image_to_string(Image.open('temp2.png'))
# os.remove('temp.jpg')
print(text)

my_file = open("/home/willian/Desktop/tesserpython/capchadeth.txt", "w+")
my_file.write(text)
my_file.close()
