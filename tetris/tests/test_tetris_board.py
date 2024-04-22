import random

from python.tetris.scripts.board import TetrisBoard
from python.tetris.scripts.piece import TetrisPiece


def display(board: TetrisBoard):
    state = board.state
    falling_piece = board.falling_piece

    s = [row[:] for row in state]

    if falling_piece is not None:
        for r, c in falling_piece.shape:
            s[r][c] = TetrisBoard.FULL_CELL

    print()
    for i in range(board.max_row):
        print(' | '.join(s[i]))


def test_run():
    board_height = 8
    board_width = 6

    game = TetrisBoard(board_height, board_width)

    while not game.is_over():
        # pick random piece
        p = TetrisPiece.build(TetrisPiece.SHAPES[random.randint(0, len(TetrisPiece.SHAPES) - 1)])

        # define initial position
        p.shift(random.randint(0, board_width - 4), board_width)

        # make it fall
        game.set_falling_piece(p)
        display(game)
        while game.update_falling():
            display(game)
