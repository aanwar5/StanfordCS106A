from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6

print("Hello Everyone")
print("It is I, Abdullah Anwar")
print("Welcome to Stanford CS106A Lecture 9")
print("---- Lecturer Mehran Shahami----")
print("We'll be doing Pictures today and alot of them haha")
print("Ding!")

'''This function is a function that darkens the image'''


def darker(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
    return image


''' This function is a function that makes an image purely red'''


def red(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.blue = 0
        pixel.green = 0
    return image


'''This function defines a greenscreen function for images and pictures'''


def greenscreen(mainfile, background):
    # takes out image
    image = SimpleImage(mainfile)
    # takes out background image to be put into the main image above
    back = SimpleImage(background)
    # for seeing each pixel in the image
    for pixel in image:
        # taking out the average of all the pixels
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # is your green pixel more greener than the avg intensity
        if pixel.green >= average * INTENSITY_THRESHOLD:
            # if so then overwrite the pixel in the original image
            # corresponding pixel from the background image
            x = pixel.x
            y = pixel.y
            # set background image in those specific pixels which
            # are greener than average and replace them
            image.set_pixel(x, y, back.get_pixel(x, y))
        return image


''' This function defines a red screen function for imgs and pictures'''


def redscreen(mainfile, background):
    # takes out image
    image = SimpleImage(mainfile)
    # takes out background image to be put into the main image above
    back = SimpleImage(background)
    # for seeing each pixel in the image
    for pixel in image:
        # taking out the average of all the pixels
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # is your green pixel more greener than the avg intensity
        if pixel.red >= average * INTENSITY_THRESHOLD:
            # if so then overwrite the pixel in the original image
            # corresponding pixel from the background image
            x = pixel.x
            y = pixel.y
            # set background image in those specific pixels which
            # are greener than average and replace them
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image


def imgfunc():
    """ This opens up the original flower"""
    original_flower = SimpleImage('images/flower.png')
    original_flower.show()
    ''' This makes a darker image of a flower'''
    dark_flower = darker('images/flower.png')
    dark_flower.show()
    ''' This makes a red channel of the picture'''
    red_flower = red('images/flower.png')
    red_flower.show()


'''This function below makes a mirror of an image'''


def mirror_image(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    '''Creating a new image to contain mirror reflectin'''
    '''Still makes 1 image, not 2, you'll get this'''
    mirror = SimpleImage.blank(width * 2, height)

    '''Implementing Nested Loops for this function'''
    for y in range(height):  # looks at the y axis
        for x in range(width):  # goes through all x axis while y is still at first value
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)
    return mirror


'''red screen function example'''


def r_e_d_example():
    """The following code will be used for Green screening"""
    '''Replacing Green pixels in corresponding x, y location
    in another image'''

    original_stop = SimpleImage('images/stop.png')
    original_stop.show()

    original_leaves = SimpleImage('images/leaves.png')
    original_leaves.show()

    new_red_screen = redscreen('images/stop.png', 'images/leaves.png')
    new_red_screen.show()


def main():
    original = SimpleImage('images/abdullah.jpg')
    original.show()

    mirrored_burrito = mirror_image('images/abdullah.jpg')
    mirrored_burrito.show()


if __name__ == '__main__':
    main()
