import random


class TetrisPiece:

    SHAPES = ['s_shape', 'b_shape', 't_shape', 'p_shape', 'l_shape']

    def __init__(self, shape: [(int, int)]):
        self.shape = shape

    @staticmethod
    def build(piece_format: str):
        match piece_format:
            case 's_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])
            case 'b_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 0), (1, 1)])
            case 't_shape':
                return TetrisPiece([(0, 1), (1, 0), (1, 1), (1, 2)])
            case 'p_shape':
                return TetrisPiece([(0, 0), (1, 0), (2, 0), (3, 0)])
            case 'l_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 0), (2, 0)])

    def shift(self, x: int):
        for i, (r, c) in enumerate(self.shape):
            self.shape[i] = (r, c + x)

    def fall_once(self, max_row) -> [(int, int)]:
        new_positions = []
        for row, col in self.shape:
            if row + 1 > max_row - 1:
                return []
            new_positions.append((row + 1, col))
        return new_positions


class TetrisBoard:

    EMPTY_CELL = '_'
    FULL_CELL = 'X'

    def __init__(self, height, width):
        self.max_row = height
        self.max_col = width
        self.pieces = []
        self.falling_piece = None
        self.state = [[self.EMPTY_CELL] * self.max_col for _ in range(self.max_row)]

    def display(self):
        s = [row[:] for row in self.state]

        if self.falling_piece is not None:
            for r, c in self.falling_piece.shape:
                s[r][c] = self.FULL_CELL

        print()
        for i in range(self.max_row):
            print(' | '.join(s[i]))

    def add(self, piece: TetrisPiece):
        self.pieces.append(piece)
        for r, c in piece.shape:
            self.state[r][c] = self.FULL_CELL

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


if __name__ == '__main__':
    board_height = 10
    board_width = 10

    game = TetrisBoard(board_height, board_width)

    while not game.is_over():
        # pick random piece
        p = TetrisPiece.build(TetrisPiece.SHAPES[random.randint(0, len(TetrisPiece.SHAPES) - 1)])

        # define initial position
        p.shift(random.randint(0, board_width - 4))

        # make it fall
        game.set_falling_piece(p)
        game.display()
        while game.update_falling():
            game.display()
