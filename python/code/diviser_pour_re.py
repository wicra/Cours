from PIL import Image

img = Image.open("joconde_1024.png")
img.show()
img.size

def echange_pixels(image: PIL.image,
                   x0: int, y0: int,
                   x1: int, y1: int) -> PIL.image:
    couleurs0, couleurs1 = image.getpixel(x0, y0), image.getpixel(x1, y1)
    image.putpixel(x0, y0, couleurs1)
    image.putpixel(x1, y1, couleurs0)
    return image