from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(20,780,5):
        draw_boy(x,550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 40, -5):
        draw_boy(780, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(780,20,-5):
        draw_boy(x,40)
    pass


def move_left():
    print('Moving left')
    for y in range(40, 550, 5):
        draw_boy(20, y)
    pass


def move_rectangle():
    print("move_rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("move_circle")
    r=200
    for deg in range(0,360):
        x= r * math.cos(math.radians(deg)) + 400
        y= r * math.sin(math.radians(deg)) + 300

        draw_boy(x, y)

    pass


def bottom_triangle():
    pass


def right_triangle():
    pass


def left_triangle():
    pass


def move_triangle():
    print("move_triangle")
    bottom_triangle()
    right_triangle()
    left_triangle()
    
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # move_rectangle()
    # move_circle()
    move_triangle()
    break
    pass



close_canvas()
