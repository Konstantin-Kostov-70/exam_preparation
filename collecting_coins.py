from math import floor


def get_next_position(f_row, f_col, f_size, com):
    if com == 'up':
        if f_row - 1 >= 0:
            f_row -= 1
        else:
            f_row = size - 1
        return f_row, f_col

    if com == 'down':
        if f_row + 1 < f_size:
            f_row += 1
        else:
            f_row = 0
        return f_row, f_col

    if com == 'left':
        if f_col - 1 >= 0:
            f_col -= 1
        else:
            f_col = f_size - 1
        return f_row, f_col

    if com == 'right':
        if f_col + 1 < f_size:
            f_col += 1
        else:
            f_col = 0
        return f_row, f_col


size = int(input())
matrix = []
all_movies = []

player_row = 0
player_col = 0
total_coin = 0
yuo_win = True

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col
            all_movies.append([player_row, player_col])
            matrix[row][col] = 0

while total_coin < 100:
    command = input()

    player_row, player_col = get_next_position(player_row, player_col, size, command)
    all_movies.append([player_row, player_col])

    if matrix[player_row][player_col] == 'X':
        yuo_win = False
        total_coin /= 2
        break
    else:
        total_coin += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = 0


if yuo_win:
    print(f"You won! You've collected {total_coin} coins.")
else:
    print(f"Game over! You've collected {floor(total_coin)} coins.")

print("Your path:")
[print(x) for x in all_movies]

