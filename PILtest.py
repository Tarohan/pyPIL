# cording utf-8
from PIL import Image, ImageFilter
import math

a = Image.open('test.jpg')

if int(a.height) > 540:
    a = a.resize((math.ceil(a.width / 2), math.ceil(a.height / 2)), Image.LANCZOS)

canvas = Image.new('RGB', (a.width, a.height * 2), (255, 255, 255))

canvas.paste(a, (0, 0))
# a = a.convert("L")  # グレイスケール変換
a = a.filter(ImageFilter.SHARPEN)  # シャープネスフィルター
canvas.paste(a, (0, int(a.height)))

canvas.save('test2.jpg', 'JPEG', quality=100, optimize=True)
