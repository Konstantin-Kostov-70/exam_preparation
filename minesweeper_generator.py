import ast


def around_bomb(f_row, f_col, f_matrix, f_size):
    # up
    if f_row - 1 >= 0:
        if not matrix[f_row - 1][f_col] == '*':
            matrix[f_row - 1][f_col] += 1
    # down
    if f_row + 1 < f_size:
        if not matrix[f_row + 1][f_col] == '*':
            matrix[f_row + 1][f_col] += 1
    # left
    if f_col - 1 >= 0:
        if not matrix[f_row][f_col - 1] == '*':
            matrix[f_row][f_col - 1] += 1
    # right
    if f_col + 1 < f_size:
        if not matrix[f_row][f_col + 1] == '*':
            matrix[f_row][f_col + 1] += 1
    # up_left
    if f_row - 1 >= 0 and f_col - 1 >= 0:
        if not matrix[f_row - 1][f_col - 1] == '*':
            matrix[f_row - 1][f_col - 1] += 1
    # up_right
    if f_row - 1 >= 0 and f_col + 1 < f_size:
        if not matrix[f_row - 1][f_col + 1] == '*':
            matrix[f_row - 1][f_col + 1] += 1
    # down_left
    if f_row + 1 < f_size and f_col - 1 >= 0:
        if not matrix[f_row + 1][f_col - 1] == '*':
            matrix[f_row + 1][f_col - 1] += 1
    # down_right
    if f_row + 1 < f_size and f_col + 1 < f_size:
        if not matrix[f_row + 1][f_col + 1] == '*':
            matrix[f_row + 1][f_col + 1] += 1

    return f_matrix


size = int(input())
nums_of_bombs = int(input())
matrix = []

for row in range(size):
    current_row = []
    for col in range(size):
        current_row.append(0)
    matrix.append(current_row)

for _ in range(nums_of_bombs):
    bomb_row, bomb_col = ast.literal_eval(input())
    matrix[bomb_row][bomb_col] = '*'
    matrix = around_bomb(bomb_row, bomb_col, matrix, size)

[print(' '.join([str(y) for y in x]))for x in matrix]


