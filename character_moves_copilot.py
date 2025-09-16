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

def move_triangle():
    print("move_triangle")
    # 삼각형 꼭짓점 좌표
    x1, y1 = 400, 550   # 위쪽 꼭짓점
    x2, y2 = 750, 50    # 오른쪽 아래 꼭짓점
    x3, y3 = 50, 50     # 왼쪽 아래 꼭짓점
    steps = 100

    # 1번 변: 위 -> 오른쪽 아래
    for i in range(steps + 1):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        draw_boy(x, y)
    # 2번 변: 오른쪽 아래 -> 왼쪽 아래
    for i in range(steps + 1):
        x = x2 + (x3 - x2) * i / steps
        y = y2 + (y3 - y2) * i / steps
        draw_boy(x, y)
    # 3번 변: 왼쪽 아래 -> 위
    for i in range(steps + 1):
        x = x3 + (x1 - x3) * i / steps
        y = y3 + (y1 - y3) * i / steps
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()
