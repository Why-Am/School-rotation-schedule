from sys import argv

import pygame as pg

from buttons import Button
from schedule import *
from ui_constants import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("School rotation schedule")
clock = pg.time.Clock()
running = True

schedule = Schedule(argv[1])

buttons = [
    Button(
        "<", pg.Rect(0, 0, BUTTON_W, BUTTON_H), "grey", callback=schedule.show_prev_week
    ),
    Button(
        ">",
        pg.Rect(WIDTH - BUTTON_W, 0, BUTTON_W, BUTTON_H),
        "grey",
        callback=schedule.show_next_week,
    ),
]


def draw() -> None:
    print("Drew")
    screen.fill("white")

    for button in buttons:
        button.draw(screen)

    schedule.draw_text()  # Bruh
    screen.blit(schedule.text_surface, schedule.text_rect)
    pg.display.flip()


draw()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            for button in buttons:
                button.handle_press()
            draw()  # draws only when mouse clicked for "efficiency"

    clock.tick(60)

pg.quit()
