def get_next_position(f_row, f_col, f_rows, f_cols, com):
    if com == 'up':
        if f_row - 1 >= 0:
            f_row -= 1
        else:
            f_row = f_rows - 1
        return f_row, f_col

    if com == 'down':
        if f_row + 1 < f_rows:
            f_row += 1
        else:
            f_row = 0
        return f_row, f_col

    if com == 'left':
        if f_col - 1 >= 0:
            f_col -= 1
        else:
            f_col = f_cols - 1
        return f_row, f_col

    if com == 'right':
        if f_col + 1 < cols:
            f_col += 1
        else:
            f_col = 0
        return f_row, f_col


rows, cols = [int(x) for x in input().split(', ')]
matrix = []

all_gifts = -1
decorations = 0
gifts = 0
cookies = 0
found_all_gifts = False


santa_row = 0
santa_col = 0

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(cols):
        if matrix[row][col] == 'Y':
            santa_row, santa_col = row, col
        if not matrix[row][col] == '.':
            all_gifts += 1

command = input()

while not command == 'End':
    direction, step = command.split('-')

    for _ in range(int(step)):

        next_santa_row, next_santa_col = get_next_position(santa_row, santa_col, rows, cols, direction)

        matrix[santa_row][santa_col] = 'x'
        santa_row, santa_col = next_santa_row, next_santa_col

        if matrix[santa_row][santa_col] == 'D':
            decorations += 1
            all_gifts -= 1

        elif matrix[santa_row][santa_col] == 'G':
            gifts += 1
            all_gifts -= 1

        elif matrix[santa_row][santa_col] == 'C':
            cookies += 1
            all_gifts -= 1

        matrix[santa_row][santa_col] = 'Y'

        if all_gifts == 0:
            found_all_gifts = True
            print("Merry Christmas!")
            break
    if found_all_gifts:
        break
    command = input()

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for el in matrix:
    print(' '.join(el))
