import pygame, random

from sudoku_generator import generate_sudoku
from cell import Cell

class Board:
    size = 9
    thickness = 5
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.sudoku = generate_sudoku(self.size, difficulty)
        self.original = self.sudoku
        for r in range(len(self.sudoku)):
            self.cells.append([])
            for c in range(len(self.sudoku)):
                self.cells[r].append(Cell(self.sudoku[r][c], r, c, self.screen))
        self.selectR = -1
        self.selectC = -1
#
    def draw(self):
        # print("Drawing Board")
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                self.cells[r][c].draw(r*self.width//len(self.sudoku), c*self.height//len(self.sudoku), self.width/len(self.sudoku), self.height/len(self.sudoku))

        pygame.draw.line(self.screen, pygame.Color("black"), (0, 0),(self.width, 0), self.thickness)
        pygame.draw.line(self.screen, pygame.Color("black"), (0, 0),(0, self.height), self.thickness)
        pygame.draw.line(self.screen, pygame.Color("black"), (0, self.height), (self.width, self.height), self.thickness)
        pygame.draw.line(self.screen, pygame.Color("black"), (self.width, 0), (self.width, self.height), self.thickness)

        for box_col in range(0, self.width, self.width//int(len(self.sudoku)**(1/2))):
            pygame.draw.line(self.screen, pygame.Color("black"), (box_col, 0), (box_col, self.height), self.thickness)
        for box_row in range(0, self.height, self.height//int(len(self.sudoku)**(1/2))):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, box_row), (self.width, box_row), self.thickness)

    def select(self, row, col):
        self.selectR = row
        self.selectC = col
        self.cells[row][col].set_selected(True)

    def unselect(self):
        self.cells[self.selectR][self.selectC].set_selected(False)

    def click(self, x, y):
        return x*len(self.sudoku)//self.width, y*len(self.sudoku)//self.height

    def clear(self):
        if self.cells[self.selectR][self.selectC].selected:
            if self.original[self.selectR][self.selectC] == 0:
                self.cells[self.selectR][self.selectC].set_cell_value(0)

    def sketch(self, value):
        if self.cells[self.selectR][self.selectC].selected:
            self.cells[self.selectR][self.selectC].set_sketched_value(value)

    def place_number(self, value):
        if self.cells[self.selectR][self.selectC].selected:
            self.cells[self.selectR][self.selectC].set_cell_value(value)

    def reset_to_original(self):
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                self.cells[r][c].set_cell_value(self.original[r][c])

    def is_full(self):
        if self.find_empty == (-1, -1):
            return True
        return False

    def update_board(self):
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                self.sudoku[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                if self.sudoku[r][c] == 0:
                    return r, c
        return -1, -1

    def check_board(self):
        self.update_board()
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                #check row
                for other_c in range(len(self.sudoku)):
                    if c != other_c and self.sudoku[r][c] == self.sudoku[r][other_c]:
                        return False
                # check column
                for other_r in range(len(self.sudoku)):
                    if r != other_r and self.sudoku[r][c] == self.sudoku[other_r][c]:
                        return False
                # check box
                for box_r in range(r//(len(self.sudoku)**(1/2))*(len(self.sudoku)**(1/2)), r//(len(self.sudoku)**(1/2))*(len(self.sudoku)+(len(self.sudoku)))):
                    for box_c in range(c//(len(self.sudoku)**(1/2))*(len(self.sudoku)**(1/2)), c//(len(self.sudoku)**(1/2))*(len(self.sudoku)+(len(self.sudoku)))):
                        if (r != box_r and c != box_c) and self.sudoku[r][c] == self.sudoku[box_r][box_c]:
                            return False
        return True






