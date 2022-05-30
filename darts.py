import ast


def get_result(f_row, f_col, f_matrix, f_size):
    f_result = 0
    is_bull = False

    if f_matrix[f_row][f_col].isdigit():
        f_result += int(f_matrix[f_row][f_col])
        return f_result, is_bull

    if f_matrix[f_row][f_col] == 'B':
        is_bull = True
        return f_result, is_bull

    if f_matrix[f_row][f_col] == 'D':
        f_result += (int(matrix[f_row][0]) + int(matrix[f_row][f_size - 1])
                     + int(matrix[0][f_col]) + int(matrix[f_size - 1][f_col])) * 2
        return f_result, is_bull

    if f_matrix[f_row][f_col] == 'T':
        f_result += (int(matrix[f_row][0]) + int(matrix[f_row][f_size - 1])
                     + int(matrix[0][f_col]) + int(matrix[f_size - 1][f_col])) * 3
        return f_result, is_bull


size = 7
first_player, second_player = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(size)]

turns_first = 0
turns_second = 0

points_first = 501
points_second = 501

is_bulls_eye = False
first_win = False
second_win = False

throw_counter = 0

while True:
    coords = input()
    if not coords:
        break

    row, col = ast.literal_eval(coords)
    throw_counter += 1

    if row < 0 or row >= size or col < 0 or col >= size:
        continue
    position = matrix[row][col]
    result, is_bulls_eye = get_result(row, col, matrix, size)

    if not throw_counter % 2 == 0:
        turns_first += 1
        if is_bulls_eye:
            first_win = True
            break

        points_first -= result

        if points_first <= 0:
            first_win = True
            break

    else:
        turns_second += 1

        if is_bulls_eye:
            second_win = True
            break
        points_second -= result

        if points_second <= 0:
            second_win = True
            break

if first_win:
    print(f"{first_player} won the game with {turns_first} throws!")

elif second_win:
    print(f"{second_player} won the game with {turns_second} throws!")

else:
    if points_first < points_second:
        print(f"{first_player} won the game with {turns_first} throws!")
    else:
        print(f"{second_player} won the game with {turns_second} throws!")





