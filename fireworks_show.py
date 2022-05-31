from collections import deque

effect = deque([int(x) for x in input().split(', ')])
power = [int(x) for x in input().split(', ')]

palm = 0
willow = 0
crossette = 0
is_ready = False

while effect and power:
    current_effect = effect.popleft()
    current_power = power.pop()

    if current_effect <= 0 and current_power <= 0:
        continue

    elif current_effect <= 0:
        power.append(current_power)

    elif current_power <= 0:
        effect.appendleft(current_effect)

    else:
        current_sum = current_effect + current_power

        if current_sum % 3 == 0 and not current_sum % 5 == 0:
            palm += 1

        elif current_sum % 5 == 0 and not current_sum % 3 == 0:
            willow += 1

        elif current_sum % 15 == 0:
            crossette += 1

        else:
            current_effect -= 1
            effect.append(current_effect)
            power.append(current_power)

        if palm >= 3 and willow >= 3 and crossette >= 3:
            is_ready = True
            break


if is_ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in effect)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
