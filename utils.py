import yaml
import json

yaml_file = yaml.safe_load(open('config.yaml'))

def get_letters():
    return yaml_file['letters']

def get_max_trials():
    return yaml_file['max_trials']

def get_max_swaps():
    return yaml_file['max_swaps']

def open_matrix(matrix_path = 'matrix.json'):
    with open(matrix_path, "r") as f:
        return json.loads(f.read())


def score(new_letters, input_string, matrix):
    original_letters = get_letters()
    candidate = transform_text(input_string, new_letters, original_letters)
    print("candidate ", candidate)

    showed_pairs = set()

    scr = 0
    candidate_len = len(candidate)
    print("candidate_len ", candidate_len)

    for (i, letter) in enumerate(candidate):
        index_first = original_letters.index(letter)
        print("letter  ", letter, ", index_first ", index_first)
        if i != (candidate_len - 1):
            print("i != (candidate_len - 1)  ")
            index_next = original_letters.index(candidate[i+1])
            print("index_next " , index_next)
            pair = letter + candidate[i+1]
            print("pair " , pair)
            if pair not in showed_pairs:
                showed_pairs.add(pair)
                scr += candidate.count(pair) * matrix[index_first][index_next]
                print("matrix[index_first][index_next] " , matrix[index_first][index_next])

    return scr

def transform_text(cipherText, key, original_letters):
    new_text = ''
    for letter in cipherText:
        new_text += original_letters[key.index(letter)]
    return new_text