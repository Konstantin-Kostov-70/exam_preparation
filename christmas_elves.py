from collections import deque


def not_energy():
    elves.append(current_elv * 2)
    boxes.append(toys_energy)


elves = deque(int(x) for x in input().split())
boxes = [int(x) for x in input().split()]

toys = 0
total_energy = 0
counter = 0

while elves and boxes:

    toys_energy = boxes.pop()
    current_elv = elves.popleft()

    if current_elv < 5:
        boxes.append(toys_energy)
        continue

    counter += 1

    if counter % 3 == 0:

        if current_elv - (toys_energy * 2) >= 0:
            toys += 2
            total_energy += toys_energy * 2
            elves.append(current_elv - (2 * toys_energy) + 1)
        else:
            not_energy()

    elif counter % 5 == 0:

        if current_elv - toys_energy >= 0:
            total_energy += toys_energy
            elves.append(current_elv - toys_energy)
        else:
            not_energy()

    elif counter % 15 == 0:

        if current_elv - (toys_energy * 2) >= 0:
            total_energy += toys_energy * 2
            elves.append(current_elv - (2 * toys_energy) + 1)
        else:
            not_energy()

    else:

        if current_elv - toys_energy >= 0:
            total_energy += toys_energy
            toys += 1
            elves.append(current_elv - toys_energy + 1)
        else:
            not_energy()

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
else:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
