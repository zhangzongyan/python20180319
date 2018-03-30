
from PIL import Image

im = Image.open("gf.gif")

im.save("pic{:02}.png".format(im.tell()))
try:
	while True:
		im.seek(im.tell() + 1)
		im.save("pic{:02}.png".format(im.tell()))
except:
	print("处理完成")

