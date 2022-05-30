import ast

size = 6
matrix = [[x for x in input().split()] for _ in range(size)]

points = 0
prize = ''
buckets_coords = []

for _ in range(3):
    coords = input()
    row, col = ast.literal_eval(coords)

    current_sum = 0

    if 0 <= row < size and 0 <= col < size:
        position = matrix[row][col]
        if position == "B" and coords not in buckets_coords:
            buckets_coords.append(coords)

            for el in range(size):
                if not matrix[el][col] == 'B':
                    current_sum += int(matrix[el][col])
            points += current_sum

if points > 99:
    if 100 <= points <= 199:
        prize = 'Football'
    elif 200 <= points <= 299:
        prize = 'Teddy Bear'
    elif points >= 300:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {points} points, and you've won {prize}.")

else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
