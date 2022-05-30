def get_next_position(f_row, f_col, f_size, com):
    if com == 'up':
        if f_row - 1 >= 0:
            f_row -= 1
        else:
            f_row = f_size - 1
        return f_row, f_col

    if com == 'down':
        if f_row + 1 < size:
            f_row += 1
        else:
            f_row = 0
        return f_row, f_col

    if com == 'left':
        if f_col - 1 >= 0:
            f_col -= 1
        else:
            f_col = size - 1
        return f_row, f_col

    if com == 'right':
        if f_col + 1 < size:
            f_col += 1
        else:
            f_col = 0
        return f_row, f_col


size = 6
matrix = []

rover_row = 0
rover_col = 0

water = 0
metal = 0
concrete = 0

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size):
        if matrix[row][col] == 'E':
            rover_row, rover_col = row, col

commands = input().split(', ')

for command in commands:

    rover_row, rover_col = get_next_position(rover_row, rover_col, size, command)

    rover_position = matrix[rover_row][rover_col]

    if rover_position == 'W':
        water += 1
        matrix[rover_row][rover_col] = '-'
        print(f"Water deposit found at {(rover_row,rover_col)}")

    elif rover_position == 'M':
        metal += 1
        matrix[rover_row][rover_col] = '-'
        print(f"Metal deposit found at {(rover_row,rover_col)}")

    elif rover_position == 'C':
        concrete += 1
        matrix[rover_row][rover_col] = '-'
        print(f"Concrete deposit found at {(rover_row,rover_col)}")

    elif rover_position == 'R':
        matrix[rover_row][rover_col] = '-'
        print(f"Rover got broken at {(rover_row,rover_col)}")
        break

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")



