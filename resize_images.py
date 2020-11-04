# Simple .py script that resizes images and saves them in a newly created directory

# Author: ChristinaDelta
# August 2019


import PIL
from PIL import Image
import os
import sys


# the functions resizes images and saves them
def resizeImage(infile, output_dir="", size=([252, 252])):
    outfile = os.path.splitext(infile)[0]  # e.g. stim01_resized
    extension = os.path.splitext(infile)[1]  # .png

    if infile != outfile:
        try:
            output_path = os.path.join(output_dir, outfile + extension)
            print(output_path)
            im = Image.open(infile)
            im.thumbnail((size), PIL.Image.ANTIALIAS)
            im.save(output_path)  # e.g stim01_resized.png
        except IOError as ioe:
            print("cannot reduce image for ", infile)


# create a new directory for the resized images and move them there
if __name__ == "__main__":
    output_dir = "resized"
    dir = os.getcwd()
    print(dir)


    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        extension = os.path.splitext(file)[1]
        if extension == '.png':
            resizeImage(file, output_dir)
