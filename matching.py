from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:

    if not males[-1] == 0 and males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue

    if not females[0] == 0 and females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        continue

    current_males = males.pop()
    current_females = females.popleft()

    if current_males <= 0:
        females.appendleft(current_females)
        continue

    if current_females <= 0:
        males.append(current_males)
        continue

    if not current_males == current_females:
        current_males -= 2
        males.append(current_males)
    else:
        matches += 1

males = list(reversed(males))

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print(f"Females left: none")



