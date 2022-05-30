from collections import deque

pizzas = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

order_counter = 0

while pizzas and employees:

    pizzas_order = pizzas.popleft()
    current_employer = employees.pop()

    if pizzas_order <= 0 or pizzas_order > 10:
        employees.append(current_employer)
        continue

    if pizzas_order - current_employer > 0:
        pizzas_order -= current_employer
        pizzas.appendleft(pizzas_order)
        order_counter += current_employer
    else:
        order_counter += pizzas_order

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizzas])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {order_counter}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")






