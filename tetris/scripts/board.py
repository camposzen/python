from python.tetris.scripts.piece import TetrisPiece


class TetrisBoard:
    EMPTY_CELL = '_'
    FULL_CELL = 'X'

    def __init__(self, height, width):
        self.max_row = height
        self.max_col = width
        self.pieces = []
        self.falling_piece = None
        self.state = [[self.EMPTY_CELL] * self.max_col for _ in range(self.max_row)]

    def add(self, piece: TetrisPiece):
        new_state = [[self.EMPTY_CELL] * self.max_col for _ in range(self.max_row)]
        # place new piece
        for r, c in piece.shape:
            self.state[r][c] = self.FULL_CELL
        # remove rows with all cells full
        shift_y = 0
        for i in range(self.max_row - 1, -1, -1):
            row = self.state[i]
            if self.EMPTY_CELL in row:
                new_state[i + shift_y] = row
            else:
                shift_y += 1
        self.state = new_state

    def collision(self, positions: [(int, int)]) -> bool:
        for row, col in positions:
            if self.state[row][col] == self.FULL_CELL:
                return True
        return False

    def set_falling_piece(self, piece: TetrisPiece):
        self.falling_piece = piece

    def update_falling(self):
        if self.falling_piece is None:
            return False

        new_positions = self.falling_piece.fall_once(self.max_row)
        if not new_positions or self.collision(new_positions):
            self.add(self.falling_piece)
            return False
        else:
            self.falling_piece.shape = new_positions
            return True

    def is_over(self):
        for cell in self.state[0]:
            if cell == self.FULL_CELL:
                return True
        return False
