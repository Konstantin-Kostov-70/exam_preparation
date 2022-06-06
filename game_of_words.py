def get_next_position(f_row, f_col, f_size, com):
    pop_last = False
    if com == 'up':
        if f_row - 1 >= 0:
            f_row -= 1
        else:
            pop_last = True
        return f_row, f_col, pop_last

    if com == 'down':
        if f_row + 1 < f_size:
            f_row += 1
        else:
            pop_last = True
        return f_row, f_col, pop_last

    if com == 'left':
        if f_col - 1 >= 0:
            f_col -= 1
        else:
            pop_last = True
        return f_row, f_col, pop_last

    if com == 'right':
        if f_col + 1 < f_size:
            f_col += 1
        else:
            pop_last = True
        return f_row, f_col, pop_last


text = input()
size = int(input())
matrix = []

player_row = 0
player_col = 0

for row in range(size):
    current_row = [x for x in input()]
    matrix.append(current_row)
    for col in range(size):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col

num_of_commands = int(input())

for _ in range(num_of_commands):
    command = input()

    next_row, next_col, pop_last_char = get_next_position(player_row, player_col, size, command)
    if pop_last_char and text:
        text = text[:-1]
    else:
        if not matrix[next_row][next_col] == '-':
            text += matrix[next_row][next_col]

        matrix[player_row][player_col] = '-'

        player_row, player_col = next_row, next_col

        matrix[player_row][player_col] = 'P'

print(text)
[print(''.join(x)) for x in matrix]
