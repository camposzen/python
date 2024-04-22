import random
import tkinter

from tkinter import *

from python.tetris.scripts.board import TetrisBoard
from python.tetris.scripts.piece import TetrisPiece


class TetrisUI:

    def __init__(self, board: TetrisBoard):
        self.cells = [[]]
        self.board = board

        self.window = Tk()
        self.window.minsize(width=300, height=400)

        canvas = Canvas(width=300, height=380)
        self.fill_canvas(canvas)
        canvas.grid(row=0, column=0)

        canvas2 = Canvas()
        canvas2.grid(row=1, column=0)

        self.rotate_button = Button(master=canvas2, text='rotate', command=self.rotate_clicked, width=5, height=2)
        self.rotate_button.grid(row=1, column=1)

        self.left_button = Button(master=canvas2, text='left', command=self.left_clicked, width=5, height=2)
        self.left_button.grid(row=1, column=0)

        self.right_button = Button(master=canvas2, text='right', command=self.right_clicked, width=5, height=2)
        self.right_button.grid(row=1, column=2)

        self.update_board()
        self.window.mainloop()

    def display_score(self):
        self.right_button["state"] = "disabled"
        self.left_button["state"] = "disabled"
        self.rotate_button["state"] = "disabled"
        # TODO: display score

    def rotate_clicked(self):
        self.board.falling_piece.rotate()

    def left_clicked(self):
        self.board.falling_piece.shift(-1, self.board.max_col)

    def right_clicked(self):
        self.board.falling_piece.shift(1, self.board.max_col)

    def fill_canvas(self, canvas: tkinter.Canvas):
        for i in range(self.board.max_row):
            self.cells.append([])
            for j in range(self.board.max_col):
                e = Entry(canvas, width=2,
                          background='white' if self.board.state[i][j] == TetrisBoard.EMPTY_CELL else 'black')
                e.grid(row=i, column=j)
                self.cells[i].append(e)

    def refresh_canvas(self):
        # erase the last move
        for i in range(self.board.max_row):
            for j in range(self.board.max_col):
                self.cells[i][j].configure(
                    background='white' if self.board.state[i][j] == TetrisBoard.EMPTY_CELL else 'black')
        # include current move
        for row, col in self.board.falling_piece.shape:
            self.cells[int(row)][int(col)].configure(background='black')

    def update_board(self):
        if self.board.is_over():
            self.display_score()
            return

        # if last piece is still falling
        if not self.board.update_falling():
            # pick random piece
            p = TetrisPiece.build(TetrisPiece.SHAPES[random.randint(0, len(TetrisPiece.SHAPES) - 1)])
            # define initial position (-4 to keep the whole piece within the board area)
            p.shift(random.randint(0, self.board.max_col - 4), self.board.max_col)
            # make it fall
            self.board.set_falling_piece(p)

        self.refresh_canvas()  # TODO: fix bug printing piece after the game over
        self.window.after(1000, self.update_board)