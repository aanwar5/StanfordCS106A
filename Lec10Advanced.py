""" Graphics Advanced Python"""
'''Taking the first steps into learning Graphical Progs'''

'''Draw a Rectangle'''

import tkinter
from PIL import ImageTk
from PIL import Image

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def mouse_moved(event):
    print('x = ' + str(event.x), 'y = ' + str(event.y))


def make_canvas(width, height, title=None):

    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()

    canvas.bind("<Motion>", mouse_moved)
    return canvas

    pass


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Awesome')
    canvas.create_line(0, 0, 600, 600)

    canvas.create_rectangle(70, 70, 150, 150, fill='blue')
    canvas.create_rectangle(620, 100, 640, 510, fill='yellow')

    canvas.create_rectangle(250, 150, 500, 500)
    canvas.create_oval(250, 150, 500, 500, fill='red', outline='black')

    image = ImageTk.PhotoImage(Image.open('images/abdullah.jpg'))
    canvas.create_image(0, 300, anchor='nw', image=image)

    canvas.create_text(20, 200, anchor='w', font='Courier 52', text="Abdullah is awesome")
    canvas.mainloop()


if __name__ == '__main__':
    main()
