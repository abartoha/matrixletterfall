import os
import sys
import pygame as pg
from random import choice, randrange

# Determine the base directory (for bundled files)
if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundled app
    base_path = sys._MEIPASS
else:  # Running as a script
    base_path = os.path.dirname(os.path.abspath(__file__))

# Path to the font file
font_path = os.path.join(base_path, "MS_mincho.ttf")

class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else lightgreen_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(4, 40)
        self.speed = randrange(4, 10)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1920,1080
FONT_SIZE = 16
alpha_value = 0

pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font("MS_mincho.ttf", FONT_SIZE)
green_katakana = [font.render(char, True, (40, randrange(160, 256), 10)) for char in katakana]
lightgreen_katakana = [font.render(char, True, pg.Color('lightgreen')) for char in katakana]

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

indent = 0
while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    if not pg.time.get_ticks() % 20 and alpha_value < 170:
        alpha_value += 6
        surface.set_alpha(alpha_value)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            os._exit(0)
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            os._exit(0)
    pg.display.flip()
    indent += 1
    clock.tick(60)