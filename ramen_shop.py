from collections import deque

ramen = [int(x) for x in input().split(', ')]
client = deque([int(x) for x in input().split(', ')])

while ramen and client:
    current_ramen = ramen.pop()
    current_client = client.popleft()
    if current_client - current_ramen < 0:
        ramen.append(abs(current_client - current_ramen))
    elif current_client - current_ramen > 0:
        client.appendleft(current_client - current_ramen)

if client:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x)for x in client])}")
else:
    print('Great job! You served all the customers.')
    if ramen:
        print(f"Bowls of ramen left: {', '.join([str(x)for x in ramen])}")


