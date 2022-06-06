def numbers_searching(*args):
    duplicates = set()
    result = []

    for num in args:
        if args.count(num) > 1:
            duplicates.add(num)

    duplicates = list(sorted(duplicates))
    args = list(sorted(set(args)))

    for index in range(len(args)):
        if not args[index] + 1 == args[index + 1]:
            result.append(args[index] + 1)
            break

    result.append(duplicates)
    return result


# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
