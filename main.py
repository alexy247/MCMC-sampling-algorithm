import re
import json
from utils import get_letters


def create_matrix(filename, letters, letters_count):
    text = ''
    with open(filename) as file:
        text = file.read().lower()

    matrix = [[1] * letters_count for i in range(letters_count)]
    text_prepared = ''

    for symbol in text:
        if symbol in letters:
            text_prepared += symbol
        elif symbol == '\n':
            text_prepared += ' '

    text_prepared = re.sub(r'[\s]+|s' , ' ', text_prepared)

    with open('text-prepared.txt', "w") as f:
        f.write(text_prepared)
    text_prepared_len = len(text_prepared)

    for i, letter in enumerate(text_prepared):
        # Возможно представить, что первое слово идет за пробелом?
        index = letters.index(letter)

        if i != (text_prepared_len - 1):
            index_next = letters.index(text_prepared[i+1])
            matrix[index][index_next] += 1

    normalize_matrix = [[0] * letters_count for i in range(letters_count)]

    for i, column in enumerate(matrix):
        sum_val = sum(column)

        for j, val in enumerate(column):
            if val == 1:
                normalize_matrix[i][j] = 1 / sum_val
            else:
                normalize_matrix[i][j] = val / sum_val


    with open('matrix.json', "w") as f:
        f.write(json.dumps(normalize_matrix, ensure_ascii=False))


if __name__ == "__main__":
    letters = get_letters()
    letters_count = len(letters)

    # create_matrix('text-simple.txt', letters, letters_count)
    create_matrix('text.txt', letters, letters_count)