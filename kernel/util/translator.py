val=17
clrsorder=["white","light_grey","dark_grey","black","yellow","green","light_green","light_red","red","brown","magenta","lilac","cyan","dark_cyan","dark_blue","blue"]
# clrs=[0xFFFFFF,0xAAAAAA,0x555555,0x000000,0xFFFF55,0x55FF55,0xAA0000,0xAA5500,0xAA00AA,0xFF55FF,0x55FFFF,0x00AAAA,0x0000AA,0x5555FF]
# def clr(valu):
#     """Return the nearest color to valu"""
#     def closest(list: list,value) -> any:return min(list, key=lambda x:abs(x-value))
#     cl=closest(clrs,valu)
#     return [cl,clrsorder[clrs.index(cl)]]
# print(clr(0x888))

from math import sqrt

COLORS = [
    (255, 255, 255),
    (170, 170, 170),
    (85, 85, 85),
    (0, 0, 0),
    (255, 255, 85),
    (0, 170, 0),
    (85, 255, 85),
    (255, 85, 85),
    (170, 0, 0),
    (170, 85, 0),
    (170, 0, 170),
    (255, 85, 255),
    (85, 255, 255),
    (0, 170, 170),
    (85, 85, 255)
]

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
print(clrsorder[COLORS.index(closest_color((234,204,255)))])
from PIL import Image,ImageDraw,ImageFont
import math
from clr import *
def getSomeChar(h):
    chars  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-                          _+~<>i!lI;:,\"^`'. "[::-1]
    charArr = list(chars)
    l = len(charArr)
    mul = l/256
    return charArr[math.floor(h*mul)]
def draw(image):
    image = Image.open(f"{image}.jpg")
    scaleFac = 0.8
    charWidth = 10
    charHeight = 18
    w,h = image.size
    image = image.resize((int(scaleFac*w),int(scaleFac*h*(charWidth/charHeight))),Image.NEAREST)
    w,h = image.size
    pixels = image.load()
    for i in range(h):
        for j in range(w):
            r,g,b = pixels[j,i]
            grey = int((r/3+g/3+b/3))
            pixels[j,i] = (grey,grey,grey)
            exec(f"o.{clrsorder[COLORS.index(closest_color((r,g,b)))]}()")
draw("kernel/util/parrot")