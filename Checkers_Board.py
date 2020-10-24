# Drawing a Checkerboard by using double for loops
# How to make a single row line on a checkerboard
# How to make it  8 x 8
# How to color them all black and white
import tkinter
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
def draw_square(canvas, col, row):
    print('Draw Square...')
    print(col,col * SIZE)
    x = col * SIZE
    y = row * SIZE
    color = get_color(row, col)
    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color)

def get_color(row, col):
    if (row + col) % 2 == 0:
        return 'white'
    else:
        return 'black'

CANVAS_SIZE = 800  # total pixels
N_ROWS = 8  # number of rows
N_COLS = 8  # number of columns
SIZE = CANVAS_SIZE / N_ROWS - 1  # size of the canvas

def main():
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, "Chess Board")
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_square(canvas, col, row)
    canvas.mainloop()
if __name__ == '__main__':
    main()


