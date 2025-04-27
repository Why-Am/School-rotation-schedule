from sys import argv
import pygame as pg
from buttons import Button
from schedule import *

WIDTH, HEIGHT = 400, 300
BUTTON_W, BUTTON_H = 50, 50

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
running = True

schedule = Schedule(argv[1])

buttons = [
    Button('<', pg.Rect(0, 0, BUTTON_W, BUTTON_H), 'grey', callback=schedule.prev_week),
    Button('>', pg.Rect(WIDTH - BUTTON_W, 0, BUTTON_W, BUTTON_H), 'grey', callback=schedule.next_week)
]

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            for button in buttons:
                button.handle_press()

    
    screen.fill('white')

    for button in buttons:
        button.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()