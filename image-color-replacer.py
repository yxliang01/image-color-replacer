'''
Author: Xiao Liang Yu

<Image File Path> <Output Image Path> <Color to be replaced> <Replacement Color>


E.g. black.png blue.png "(0,0,0)" "(0,0,255)"
Which replace all black color pixel to blue

'''
from PIL import Image
from sys import argv
import numpy as np

NEW_IMAGE_PATH = argv[2]
TARGET_COLOR = eval(argv[3])
NEW_COLOR = eval(argv[4])

image = Image.open(argv[1])
image = image.convert('RGBA')

data = np.array(image)
red, green, blue, alpha = data.T

target_area = (red == TARGET_COLOR[0]) & (
    green == TARGET_COLOR[1]) & (blue == TARGET_COLOR[2])
data[..., :-1][target_area.T] = NEW_COLOR

out_image = Image.fromarray(data)
out_image.save(NEW_IMAGE_PATH)
