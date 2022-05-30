def words_sorting(*args):
    words = {}
    total_sum = 0
    result = ''

    for word in args:
        word_sum = 0
        for letter in word:
            word_sum += ord(letter)
        words[word] = word_sum
        total_sum += word_sum

    if not total_sum % 2 == 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: -x[1]))
    else:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[0]))

    for key, value in sorted_words.items():
        result += f"{key} - {value}\n"

    return result


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#     ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
