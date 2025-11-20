import math, random

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(row_length ** (1 / 2))
        self.board = []
        for r in range(row_length):
            self.board.append([])
            for c in range(row_length):
                self.board[r].append("-")
        self.fill_values()


    def get_board(self):
        return self.board

    def print_board(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end=" ")
            print()

    def valid_in_row(self, row, num):
        return not (num in self.board[row])

    def valid_in_col(self, col, num):
        for r in range(len(self.board)):
            if num == self.board[r][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num)
                and self.valid_in_col(col, num)
                and self.valid_in_box((row//self.box_length)*self.box_length, (col//self.box_length)*self.box_length, num))

    def fill_box(self, row_start, col_start):
        unused_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(unused_in_box)
        for r in range(row_start, row_start+self.box_length):
            for c in range(col_start, col_start+self.box_length):
                self.board[r][c] = unused_in_box.pop()

    def fill_diagonal(self):
        for b in range(self.row_length//self.box_length):
            self.fill_box(b*self.box_length, b*self.box_length)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
 
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        # removes cells to 0 with random row col coords
        for n in range(self.removed_cells):
            removed = False
            while not removed:
                r, c = random.randint(0, self.row_length-1), random.randint(0, self.row_length-1)
                if self.board[r][c] != 0:
                    self.board[r][c] = 0
                    removed = True


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board()
    return board