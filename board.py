import pygame, random

import sudoku
from cell import Cell

class Board:
    size = 9
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.sudoku = sudoku.generate_sudoku(self.size, difficulty)
        for r in range(len(self.sudoku)):
            self.cells.append([])
            for c in range(len(self.sudoku[r])):
                self.cells[r] += Cell(sudoku[r][c], r, c, self.screen)
#
    def draw(self):

        for cell in self.cells:
            cell.draw()

    def select(self, row, col):
        self.cells[row][col].select()
