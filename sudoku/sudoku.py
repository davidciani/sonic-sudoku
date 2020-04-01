from math import sqrt

# Dimension of the sudoku board
N = 9


class Board(object):
    def __init__(self, board_array):
        self.board = board_array

    def row(self, row):
        return self.board(row)

    def col(self, col):
        return [row[col] for row in self.board]

    def validate(self):

        for x in range(0, N):
            this_row = self.row(x)
            if len(this_row) != set(len(this_row)):
                return False

            this_col = self.col(x)
            if len(this_row) != set(len(this_row)):
                return False

            this_block = self.block(x)
            if len(this_block) != set(len(this_block)):
                return False


TEST_BOARD = [
    [8, 0, 0, 0, 9, 0, 0, 0, 5],
    [0, 5, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 8, 0, 0, 4, 0, 1, 0, 0],
    [0, 7, 0, 0, 2, 0, 0, 9, 0],
    [0, 0, 0, 5, 0, 3, 0, 0, 4],
    [4, 9, 0, 0, 5, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 8, 7, 5, 0, 0],
]


def main():

    current_cell = (0, 0)


if __name__ == "__main__":
    main()
