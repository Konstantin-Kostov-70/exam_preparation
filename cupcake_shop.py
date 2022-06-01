def stock_availability(inventory, action, *args):
    if action == 'delivery':
        inventory += list(args)
        return inventory

    if not args:
        return inventory[1:]

    if type(args[0]) == int:
        return inventory[args[0]:]

    sold_items = set(args)
    return [item for item in inventory if item not in sold_items]



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
