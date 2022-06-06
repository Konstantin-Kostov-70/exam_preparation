def find_queen(f_row, f_col, f_matrix, f_size):
    f_coords = []
    f_king_row, f_king_col = f_row, f_col

    # up
    while f_row > 0:
        f_row -= 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # down
    while f_row < f_size - 1:
        f_row += 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # left
    while f_col > 0:
        f_col -= 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # right
    while f_col < f_size - 1:
        f_col += 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # up_left
    while f_row > 0 and f_col > 0:
        f_row -= 1
        f_col -= 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # up_right
    while f_row > 0 and f_col < f_size - 1:
        f_row -= 1
        f_col += 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # down_left
    while f_row < f_size - 1 and f_col > 0:
        f_row += 1
        f_col -= 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    f_row, f_col = f_king_row, f_king_col

    # down-right
    while f_row < f_size - 1 and f_col < f_size - 1:
        f_row += 1
        f_col += 1
        if f_matrix[f_row][f_col] == 'Q':
            f_coords.append([f_row, f_col])
            break
    return f_coords


size = 8
matrix = []

king_row = 0
king_col = 0

coords = []

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size):
        if matrix[row][col] == 'K':
            king_row, king_col = row, col

coords = find_queen(king_row, king_col, matrix, size)
if len(coords) == 0:
    print('The king is safe!')
else:
    [print(x) for x in coords]