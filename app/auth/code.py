from PIL import Image, ImageFont, ImageDraw
import random

arr = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class AuthCode(object):
    def __init__(self,size=(100,40),fontSize=30):
        self.font = ImageFont.truetype('./Arial.ttf',fontSize)
        self.size = size
        self.image = Image.new('RGBA',self.size,(255,)*4)
        self.texts = self.random_text()

    def random_text(self,length=4):
        res = ''
        for i in range(length):
            res += arr[random.randint(0, 61)]
        return res

    def rotate(self):
        rot = self.image.rotate(random.randint(-5,5),expand=0)
        fff = Image.new('RGBA',rot.size,(255,)*4)
        self.image = Image.composite(rot,fff,rot)

    def rand_color(self):
        self.fontColor = (random.randint(0,250),random.randint(0,250),random.randint(0,250))

    def randNum(self,bits):
        return ''.join(str(random.randint(0,9)) for i in range(bits))

    def write(self,text,x):
        draw = ImageDraw.Draw(self.image)
        draw.text((x,4),text,fill=self.fontColor,font=self.font)

    def write_text(self):
        x = 10
        xplus = 15
        for text in self.texts:
            self.rand_color()
            self.write(text, x)
            self.rotate()
            x += xplus
        return self.texts

    def get_data(self):
        self.write_text()
        return (self.texts,self.image)
