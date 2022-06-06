from collections import deque

tasks = [int(x) for x in input().split(', ')]
task_index = int(input())

sorted_tasks = deque(sorted((value, index) for index, value in enumerate(tasks)))

cycles = 0

while True:
    item = sorted_tasks.popleft()
    cycles += item[0]
    if item[1] == task_index:
        break

print(cycles)



