from collections import deque
customers = deque([int(x) for x in input().split(', ')])
taxi = [int(x) for x in input().split(', ')]

total_time = 0

while customers and taxi:
    current_customers = customers.popleft()
    current_taxi = taxi.pop()

    if current_taxi - current_customers >= 0:
        total_time += current_customers
    else:
        customers.appendleft(current_customers)

if len(customers) == 0:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    customers = ', '.join([str(x) for x in customers])
    print(f"Not all customers were driven to their destinations\nCustomers left: {customers}")


