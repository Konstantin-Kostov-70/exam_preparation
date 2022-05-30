def flights(*args):
    all_flights = {}
    current_list = []

    for el in args:
        if el == 'Finish':
            break
        current_list.append(el)
        if len(current_list) == 2:
            key, value = current_list[0], current_list[1]

            if key not in all_flights:
                all_flights[key] = value
            else:
                all_flights[key] += value

            current_list = []
    return all_flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))


# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))