from PIL import Image
import matplotlib.pyplot as plt

with Image.open("/IT/Human_Pain.png") as img:
    orig_width, orig_height = img.size
    width = 80
    scale = width / orig_width
    height = int(scale * orig_height)
    img.thumbnail((width, height))

    plt.imshow(img)
    plt.show()
    values = list(img.getdata())
    pixels = [[img.getpixel((x, y)) for x in range(0, width - 1)] for y in range(0, height - 1)]
    def reshape(height, weight, lst):
        return[lst[i * weight: i * weight + weight] for i in range(height)]
    pixels = [sum(i) / 3 for i in pixels]
    pixels = reshape(height, width, values)
    chars = '@%X#*+=-:. '
    for irow, row in enumerate(pixels):
        for ipixel, pixel in enumerate(row):
            ch = pixel // 25
            plt.text(ipixel, irow, s = ch)
    plt.show()