

from PIL import Image
from PIL import ImageFilter

im = Image.open("./gg.jpg")

#om = im.filter(ImageFilter.CONTOUR)
om = im.filter(ImageFilter.SMOOTH_MORE)

om.save("gg_contour.png")



