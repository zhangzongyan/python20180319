

from PIL import Image

im = Image.open("gg.jpg")
print(im.format, im.mode, im.size)
#im.thumbnail((300, 100)) # 缩放图片
# 获取图片中rgb的值
r, g, b = im.split()
#print(r, g, b)

newb = b.point(lambda i : i * 0.5)  #设置blue
newg = g.point(lambda i : i < 100)

# 改变图片中的rgb值
om = Image.merge("RGB", (r, newg, newb))

om.save("newgg.png")

