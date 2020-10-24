"""Square Animation """
import time
import tkinter

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BALL_SIZE = 70
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20



def mouse_moved(event):
    print('x = ' + str(event.x), 'y = ' + str(event.y))


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_top_x(canvas, object):
    return canvas.coords(object)[0]


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


def hit_left_wall(canvas, object):
    return canvas.coords(object)[0] <= 0


def hit_top_wall(canvas, object):
    return canvas.coords(object)[1] <= 0


def hit_right_wall(canvas, object):
    return canvas.coords(object)[2] >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return canvas.coords(object)[3] >= CANVAS_HEIGHT

def hit_paddle(canvas, ball, paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords [0]
    y1 = paddle_coords [1]
    x2 = paddle_coords [2]
    y2 = paddle_coords [3]
    results = canvas.find_overlapping(x1,y1,x2,y2)
    return len(results)>1

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Bouncy Ball")
    start_y = 0
    PADDLE_Y = 500
    ball = canvas.create_oval(0, start_y, BALL_SIZE, start_y + BALL_SIZE, fill="blue", outline="yellow")
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 20, fill = "yellow", outline ="Blue")
    change_x = 10
    change_y = 7

    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle,mouse_x,PADDLE_Y)


        canvas.move(ball, change_x, change_y)
        if hit_bottom_wall(canvas, ball) or hit_top_wall(canvas, ball):
            change_y *= -1
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas,ball):
            change_x *=-1

        if hit_paddle(canvas, ball, paddle):
            change_y *= -1
            canvas.update()
        canvas.update()

        time.sleep(1 / 50.)



if __name__ == '__main__':
    main()
