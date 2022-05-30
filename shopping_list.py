def shopping_list(budget, **kwargs):
    result = ''
    counter = 0
    if budget < 100:
        return "You do not have enough budget."
    while budget >= 0:
        for name, value in kwargs.items():
            price = float(value[0])
            quantity = float(value[1])
            current_sum = price * quantity
            if budget - current_sum >= 0 and counter < 5:
                budget -= current_sum
                counter += 1
                result += f"You bought {name} for {current_sum:.2f} leva.\n"
            else:
                return result
        return result


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
