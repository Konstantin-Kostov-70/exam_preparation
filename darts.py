import ast


def get_result(f_row, f_col, f_matrix, f_size):
    f_result = 0

    if f_row < 0 or f_row >= size or f_col < 0 or f_col >= size:
        return f_result

    if f_matrix[f_row][f_col].isdigit():
        f_result += int(f_matrix[f_row][f_col])
        return f_result

    if f_matrix[f_row][f_col] == 'B':
        f_result = 501
        return f_result

    if f_matrix[f_row][f_col] == 'D':
        f_result += (int(matrix[f_row][0]) + int(matrix[f_row][f_size - 1])
                     + int(matrix[0][f_col]) + int(matrix[f_size - 1][f_col])) * 2
        return f_result

    if f_matrix[f_row][f_col] == 'T':
        f_result += (int(matrix[f_row][0]) + int(matrix[f_row][f_size - 1])
                     + int(matrix[0][f_col]) + int(matrix[f_size - 1][f_col])) * 3
        return f_result


size = 7
first_player, second_player = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(size)]

turns_first = 0
turns_second = 0

points_first = 501
points_second = 501

throw_counter = 0

while True:

    coords = input()
    if not coords:
        break

    row, col = ast.literal_eval(coords)

    throw_counter += 1

    result = get_result(row, col, matrix, size)

    if not throw_counter % 2 == 0:
        turns_first += 1
        points_first -= result

        if points_first <= 0:
            break

    else:
        turns_second += 1
        points_second -= result

        if points_second <= 0:
            break

if points_first < points_second:
    print(f"{first_player} won the game with {turns_first} throws!")
else:
    print(f"{second_player} won the game with {turns_second} throws!")




