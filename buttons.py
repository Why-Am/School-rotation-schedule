import pygame as pg

class Button:
    """button lol"""
    def __init__(self, text, rect, color, callback):
        self.text = text
        self.rect = rect
        self.color = color
        self.callback = callback
    
    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
    
    def handle_press(self):
        if pg.Rect.collidepoint(self.rect, pg.mouse.get_pos()):
            self.callback()
    