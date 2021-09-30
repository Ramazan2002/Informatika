import numpy as np
from PIL import Image

def img2arr(image):
	return np.array(image)

def arr2img(array2d):
	array2d = np.array(array2d)
	image = Image.fromarray(array2d.astype(np.uint8))
	image.show()

def resize(image):
	new_height = 300
	width, height = image.size
	new_width = int(width * (new_height / height))
	return image.resize((new_width, new_height))

def rgb2gray(array):
	h, w, d = array.shape
	new = [[int(sum(array[j][i]) / 3) for i in range(h)] for j in range(w)]
	return new


def array2plot(array):
	with open('new.txt', 'w', encoding='utf-8') as f:
		s = '@%#*+=-:. '
		size = round(256 / 10)
		for i in range(len(array)):
			for j in range(len(array[i])):
				c = array[i][j] // size
				print(s[c], end='', file=f)
			print(file=f)

img = Image.open('123.jpg')
# img = resize(img)
raw_image = img2arr(img)
new = rgb2gray(raw_image)
arr2img(new)
array2plot(new)