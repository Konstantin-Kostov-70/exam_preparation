def get_magic_triangle(count):
    matrix = []

    for row in range(count):
        temp_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                temp_row.append(1)
            else:
                temp_row.append(matrix[row - 1][col - 1] + matrix[row - 1][col])
        matrix.append(temp_row)

    print(matrix)


get_magic_triangle(8)