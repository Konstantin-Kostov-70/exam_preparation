from collections import deque


def gifts(f_gemstone, f_porcelain, f_gold, f_diamond, f_current_sum):
    if 100 <= f_current_sum <= 199:
        f_gemstone += 1

    elif 200 <= f_current_sum <= 299:
        f_porcelain += 1

    elif 300 <= f_current_sum <= 399:
        f_gold += 1

    elif 400 <= f_current_sum <= 499:
        f_diamond += 1

    return f_gemstone, f_porcelain, f_gold, f_diamond


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gemstone = 0
porcelain = 0
gold = 0
diamond = 0

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    current_sum = current_material + current_magic

    if current_sum < 100 or current_sum > 499:

        if current_sum < 100:
            if current_sum % 2 == 0:
                current_sum = current_material * 2 + current_magic * 3
            else:
                current_sum = (current_material + current_magic) * 2
            gemstone, porcelain, gold, diamond = gifts(gemstone, porcelain, gold, diamond, current_sum)

        else:
            current_sum = (current_material + current_magic) / 2
            gemstone, porcelain, gold, diamond = gifts(gemstone, porcelain, gold, diamond, current_sum)

    else:
        gemstone, porcelain, gold, diamond = gifts(gemstone, porcelain, gold, diamond, current_sum)

if (gemstone > 0 and porcelain > 0) or (gold > 0 and diamond > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

if diamond:
    print(f"Diamond Jewellery: {diamond}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain:
    print(f"Porcelain Sculpture: {porcelain}")



