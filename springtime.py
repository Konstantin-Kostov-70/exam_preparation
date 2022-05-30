def start_spring(**kwargs):
    result = ''
    spring = {}
    for key, value in kwargs.items():

        if value not in spring:
            spring[value] = []
        spring[value].append(key)

    for name, collection in spring.items():
        spring[name] = list(sorted(collection))

    sorted_spring = dict(sorted(spring.items(), key=lambda x: (-len(x[1]), x[0])))

    for keys, values in sorted_spring.items():
        result += f"{keys}:\n"
        for el in values:
            result += f"-{el}\n"

    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

