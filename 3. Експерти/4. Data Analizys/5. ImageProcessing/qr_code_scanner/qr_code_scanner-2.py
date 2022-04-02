import pyzbar.pyzbar as zbar
import cv2
from PIL import Image
image = 'qr_code.jpg'
barcode = zbar.decode(Image.open(image))
print('ZBar: {}'.format(barcode[0].data.decode("utf-8")))
