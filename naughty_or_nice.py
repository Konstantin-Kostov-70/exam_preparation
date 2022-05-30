def naughty_or_nice_list(*args, **kwargs):
    all_kids = {'Nice': [], 'Naughty': [], 'Not found': []}

    if kwargs:
        for key, value in kwargs.items():
            if value in all_kids:
                all_kids[value].append(key)

    kids_list, commands = args[0], list(args[1:])

    for command in commands:
        num, com = command.split('-')
        current_list = []
        for el in kids_list:
            if int(num) in el:
                current_list.append(el)
        if len(current_list) < 2:
            kids_list.remove(current_list[0])
            if current_list[0][1] not in all_kids[com]:
                all_kids[com].append(current_list[0][1])
        else:
            for elem in current_list:
                if elem[1]:
                    pass

    print()






print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
