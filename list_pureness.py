from collections import deque


def best_list_pureness(*args):
    temp_list = deque([int(x) for x in args[0]])
    count = int(args[1])
    best_pureness = -999999999999
    best_rotation = 0

    for rotation in range(count + 1):
        current_pureness = 0
        for index, value in enumerate(temp_list):
            current_pureness += index * value

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation
        temp_list.appendleft(temp_list.pop())

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)

