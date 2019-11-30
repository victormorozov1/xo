from classes import *
from constants import *
from functions import *
import pygame


class Game:
    def __init__(self):
        self.board = Board(N, N)

    def show(self):
        for i in range(self.board.n):
            for j in range(self.board.m):
                if self.board.arr[i][j].val == '-':
                    draw_empty(self.win, i * sz, j * sz, sz, sz)
                elif self.board.arr[i][j].val == 'X':
                    draw_x(self.win, i * sz, j * sz, sz, sz)
                elif self.board.arr[i][j].val == 'O':
                    draw_o(self.win, i * sz, j * sz, sz, sz)

    def run(self):
        self.running = True
        pygame.init()
        self.win = pygame.display.set_mode((SZ, SZ))
        self.show()
        while self.running:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    self.board.click(i.pos[0] // sz, i.pos[1] // sz)
            self.show()
            pygame.display.update()

