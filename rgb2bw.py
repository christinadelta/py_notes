# simple script that converts RGB images to black and white


import PIL
from PIL import Image
image_file = Image.open("img_to_be_converted.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')
