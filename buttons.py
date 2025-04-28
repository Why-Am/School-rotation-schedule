from typing import Callable
import pygame as pg


class Button:
    """button lol"""

    def __init__(
        self, text: str, rect: pg.Rect, color: str, callback: Callable[[], None]
    ) -> None:
        self.text = text
        self.rect = rect
        self.color = color
        self.callback = callback

    def draw(self, surface: pg.Surface) -> None:
        pg.draw.rect(surface, self.color, self.rect)

    def handle_press(self) -> None:
        if pg.Rect.collidepoint(self.rect, pg.mouse.get_pos()):
            self.callback()
