from PIL import Image, ImageOps


def cal_volumefraction_image(figure_name):
    img = Image.open(figure_name)
    pixels = img.getdata()
    black_thresh = 50
    nblack = sum(sum(pixel) < black_thresh for pixel in pixels)
    n = len(pixels)
    Vf = nblack / float(n)
    del img
    return Vf
