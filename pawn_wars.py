def left_white(row, col, size, matrix):
    if not col == 0 and not row - 1 < 0:
        f_left_white_diagonals = matrix[row - 1][col - 1]
        return f_left_white_diagonals


def right_white(row, col, size, matrix):
    if not col == size - 1 and not row - 1 < 0:
        f_right_white_diagonals = matrix[row - 1][col + 1]
        return f_right_white_diagonals


def left_black(row,col, size , matrix):
    if not col == size - 1 and not row + 1 == size:
        f_left_black_diagonals = matrix[row + 1][col + 1]
        return f_left_black_diagonals


def right_black(row, col, size, matrix):
    if not col == 0 and not row + 1 == size:
        f_right_black_diagonals = matrix[row + 1][col - 1]
        return f_right_black_diagonals


size = 8
white = []
black = []
matrix = []
chess_table = {}
square = ()

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number = ['8', '7', '6', '5', '4', '3', '2', '1']

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size):
        if matrix[row][col] == 'w':
            white = [row, col]
        elif matrix[row][col] == 'b':
            black = [row, col]

        key = (row, col)
        value = letter[col] + number[row]
        chess_table[key] = value

white_row, white_col = white[0], white[1]
black_row, black_col = black[0], black[1]

while True:
    left_white_diagonal = left_white(white_row, white_col, size, matrix)
    right_white_diagonal = right_white(white_row, white_col, size, matrix)

    if left_white_diagonal and left_white_diagonal == 'b':
        square = (black_row, black_col)
        print(f"Game over! White win, capture on {chess_table[square]}.")
        break

    elif right_white_diagonal and right_white_diagonal == 'b':
        square = (black_row, black_col)
        print(f"Game over! White win, capture on {chess_table[square]}.")
        break

    if white_row - 1 < 0:
        square = (white_row, white_col)
        print(f"Game over! White pawn is promoted to a queen at {chess_table[square]}.")
        break

    matrix[white_row][white_col] = '-'
    white_row -= 1
    matrix[white_row][white_col] = 'w'

    left_black_diagonal = left_black(black_row, black_col, size, matrix)
    right_black_diagonal = right_black(black_row, black_col, size, matrix)

    if left_black_diagonal and left_black_diagonal == 'w':
        square = (white_row, white_col)
        print(f"Game over! Black win, capture on {chess_table[square]}.")
        break

    elif right_black_diagonal and right_black_diagonal == 'w':
        square = (white_row, white_col)
        print(f"Game over! Black win, capture on {chess_table[square]}.")
        break

    if black_row + 1 == size:
        square = (black_row, black_col)
        print(f"Game over! Black pawn is promoted to a queen at {chess_table[square]}.")
        break

    matrix[black_row][black_col] = '-'
    black_row += 1
    matrix[black_row][black_col] = 'b'
