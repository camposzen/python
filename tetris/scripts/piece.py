class TetrisPiece:

    SHAPES = ['s_shape', 'b_shape', 't_shape', 'p_shape', 'l_shape']

    def __init__(self, shape: [(int, int)], size):
        self.shape = shape
        self.size = size
        self.x_shift = 0
        self.y_shift = 0

    @staticmethod
    def build(piece_format: str):
        match piece_format:
            case 's_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 1), (1, 2)], 3)  # 3 x 3
            case 'b_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 0), (1, 1)], 2)  # 2 x 2
            case 't_shape':
                return TetrisPiece([(0, 1), (1, 0), (1, 1), (1, 2)], 3)  # 3 x 3
            case 'p_shape':
                return TetrisPiece([(0, 0), (1, 0), (2, 0), (3, 0)], 4)  # 4 x 4
            case 'l_shape':
                return TetrisPiece([(0, 0), (0, 1), (1, 0), (2, 0)], 3)  # 3 x 3

    def shift(self, x: int, max_col: int):
        new_positions = []
        for i, (r, c) in enumerate(self.shape):
            new_c = c + x
            if -1 < new_c < max_col:
                new_positions.append((r, new_c))
            else:
                return
        self.shape = new_positions
        self.x_shift += x

    def fall_once(self, max_row: int) -> [(int, int)]:
        new_positions = []
        for row, col in self.shape:
            if row + 1 > max_row - 1:
                return []
            new_positions.append((row + 1, col))
        self.y_shift += 1
        return new_positions

    def matrix_representation(self) -> [[int]]:
        matrix = [[0] * self.size for _ in range(self.size)]
        for r, c in self.shape:
            matrix[r - self.y_shift][c - self.x_shift] = 1
        return matrix

    def rotate_matrix(self, matrix):
        border = len(matrix[0]) - 1   # self.size - 1

        # for each square border
        for x in range(0, int(self.size / 2)):

            # for each element in the 4 elements group of the current square border
            for y in range(x, border - x):
                temp = matrix[x][y]

                # from right to top
                matrix[x][y] = matrix[y][border - x]

                # from bottom to right
                matrix[y][border - x] = matrix[border - x][border - y]

                # from left to bottom
                matrix[border - x][border - y] = matrix[border - y][x]

                # assign temp to left
                matrix[border - y][x] = temp

    def rotate(self):
        matrix = self.matrix_representation()
        self.rotate_matrix(matrix)
        new_positions = []
        for r in range(self.size):
            for c in range(self.size):
                if matrix[r][c]:
                    new_positions.append((r + self.y_shift, c + self.x_shift))
        self.shape = new_positions
