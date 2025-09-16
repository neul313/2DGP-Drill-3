from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    print("move_rectangle")
    # 상단(왼->오)
    for x in range(50, 750, 5):
        draw_boy(x, 550)
    # 우측(위->아래)
    for y in range(550, 50, -5):
        draw_boy(750, y)
    # 하단(오->왼)
    for x in range(750, 50, -5):
        draw_boy(x, 50)
    # 좌측(아래->위)
    for y in range(50, 550, 5):
        draw_boy(50, y)

def move_circle():
    print("move_circle")
    r = 200
    cx, cy = 400, 300
    for deg in range(0, 360, 2):
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()
    break

close_canvas()

