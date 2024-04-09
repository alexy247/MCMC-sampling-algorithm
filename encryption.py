from random import shuffle

from utils import get_letters, open_matrix, transform_text, score

if __name__ == "__main__":
    input_string = "милый друг"
    letters = get_letters()
    matrix = open_matrix()

    shuffle_letters = letters.copy()
    shuffle(shuffle_letters)
    print(shuffle_letters)

    enncrypt_text = transform_text(input_string, shuffle_letters, letters)
    enncrypt_score = score(shuffle_letters, enncrypt_text, matrix)
    print(enncrypt_text, enncrypt_score)

    print(transform_text("вгвг аб", ["б", "г", " ", "а", "в"], ["а", "б", "в", "г", " "]))