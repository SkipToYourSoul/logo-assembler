
from PIL import Image

im = Image.open('../pictures/backend/40×30.tif')
print(im.format)
print(im.size)
print(im.mode)
print(im.info['dpi'])

tmp_image = im.transpose(Image.ROTATE_90)
tmp_image.save("./test.jpg", dpi=(300.0, 300.0))
