import pygame
from constants import *


def draw_empty(win, x, y, szx, szy):
    pygame.draw.rect(win, WHITE, (x, y, szx, szy))
    pygame.draw.rect(win, GREY, (x, y, szx, szy), 2)


def draw_x(win, x, y, szx, szy):
    draw_empty(win, x, y, szx, szy)
    pygame.draw.line(win, PLAYER_COLORS[0], (x + PADDING, y + PADDING), (x + szx - PADDING, y + szy - PADDING), WIDTH)
    pygame.draw.line(win, PLAYER_COLORS[0], (x + PADDING, y + szy - PADDING), (x + szx - PADDING, y + PADDING), WIDTH)


def draw_o(win, x, y, szx, szy):
    draw_empty(win, x, y, szx, szy)
    pygame.draw.circle(win, PLAYER_COLORS[1], (x + szx // 2, y + szy // 2), sz // 2 - PADDING, WIDTH)
