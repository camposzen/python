import tkinter
from tkinter import *


class Universe:

    def __init__(self, w: int, h: int, seed: [(int, int)]):
        self.max_row = h
        self.max_col = w

        self.board = []
        for _ in range(h):
            self.board.append([0] * w)

        self.seed(seed)

    def seed(self, positions: [(int, int)]):
        for x, y in positions:
            self.board[y][x] = 1

    def update(self):
        temp = [[0]*self.max_col for _ in range(self.max_row)]

        for r in range(self.max_row):
            for c in range(self.max_col):
                neighbors = self.count_neighbors(r, c)

                # underpopulation
                if self.board[r][c] == 1 and neighbors < 2:
                    temp[r][c] = 0

                # next generation
                elif self.board[r][c] == 1 and neighbors == 2 or neighbors == 3:
                    temp[r][c] = 1

                # overpopulation
                elif self.board[r][c] == 1 and neighbors > 3:
                    temp[r][c] = 0

                # reproduction
                elif self.board[r][c] == 0 and neighbors == 3:
                    temp[r][c] = 1

                else:
                    temp[r][c] = self.board[r][c]

        self.board = temp

    def count_neighbors(self, y: int, x: int) -> int:
        n = 0
        n += self.board[y - 1][x - 1] if (y - 1 >= 0) and (x - 1 >= 0) else 0
        n += self.board[y - 1][x] if (y - 1 >= 0) else 0
        n += self.board[y - 1][x + 1] if (y - 1 >= 0) and (x + 1 < self.max_col) else 0
        n += self.board[y][x - 1] if (x - 1 >= 0) else 0
        n += self.board[y][x + 1] if (x + 1 < self.max_col) else 0
        n += self.board[y + 1][x - 1] if (y + 1 < self.max_row) and (x - 1 >= 0) else 0
        n += self.board[y + 1][x] if (y + 1 < self.max_row) and (x + 1 < self.max_col) else 0
        n += self.board[y + 1][x + 1] if (y + 1 < self.max_row) and (x + 1 < self.max_col) else 0
        return n


class UI:

    def __init__(self, universe:Universe):
        self.cells = [[]]
        self.universe = universe

        window = Tk()
        window.minsize(width=500, height=500)

        canvas = Canvas(width=500, height=500)
        self.fill_canvas(canvas)
        canvas.pack()

        button = Button(text='go', command=self.button_clicked, width=5, height=2)
        button.pack()

        window.mainloop()

    def button_clicked(self):
        self.universe.update()
        for i in range(self.universe.max_row):
            for j in range(self.universe.max_col):
                self.cells[i][j].configure(background='white' if self.universe.board[i][j] == 0 else 'black')

    def fill_canvas(self, canvas: tkinter.Canvas):
        for i in range(self.universe.max_row):
            self.cells.append([])
            for j in range(self.universe.max_col):
                e = Entry(canvas, width=2, background='white' if self.universe.board[i][j] == 0 else 'black')
                e.grid(row=i, column=j)
                self.cells[i].append(e)


if __name__ == '__main__':
    # test with penta-decathlon oscillator
    ui = UI(
        Universe(20, 20,
                 [(4, 6), (4, 11), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (5, 10), (5, 12), (5, 13), (6, 6), (6, 11)]))

