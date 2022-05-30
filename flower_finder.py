from collections import deque


def check_char(f_vocal, f_consonant, word):
    if f_vocal in word:
        word = word.replace(f_vocal, '')
    if f_consonant in word:
        word = word.replace(f_consonant, '')
    return word


vocals = deque(input().split())
consonants = input().split()
flowers = ["rose", "tulip", "lotus", "daffodil"]
new_flowers = flowers.copy()
is_found = False
found_word = ''

while vocals and consonants:
    vocal = vocals.popleft()
    consonant = consonants.pop()

    for index in range(len(new_flowers)):
        new_flowers[index] = check_char(vocal, consonant, new_flowers[index])
        if new_flowers[index] == '':
            found_word = flowers[index]
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vocals:
    print(f"Vowels left: {' '.join(list(vocals))}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")





