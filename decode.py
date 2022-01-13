import os
from utils import get_letters, get_max_trials, get_max_swaps, open_matrix
from random import shuffle, randrange
from concurrent.futures import ThreadPoolExecutor
import time

max_threads = os.cpu_count()

input_string = "щдшэсздбгдтиылъирдвсдпирвясндждягфгдогъзд бгдсынъьисздегясздргсдовяг биъьисзднтдбнёдщдыифвсиадшсвдсвдтиыифислоиадмвжэмиадориъгаджижд бгдмыгъясиорщрвяздбгжвсвывцдявфясогббвясзадндодыгтэрзсисгддвънбдшг въибдмыншг дъвоврзбвдяжыв бвхвдыит гыидолёвънсдщдбнюнцджиждпгдусвдмврэшнрвяз"

def decode(input_string, original_letters, letters_count, max_trials, max_swaps, matrix):
    letters = original_letters.copy()

    bestScore = 0
    bestKey = letters[:]

    for i in range(0, max_trials):
        shuffle(letters)
        # bestTrialScore = 0
        # for j in range(0, max_swaps):
        new_letters = swap(letters[:], letters_count)
        newScore = score(new_letters, input_string, matrix)
        # if newScore > bestTrialScore:
        #     letters = new_letters[:]
        #     bestTrialScore = newScore
        # elif newScore == bestTrialScore:
        #     if randrange(0,2) == 1:
        #         letters = new_letters[:]
        if newScore > bestScore:
            bestKey = letters[:]
            bestScore = newScore
            print('New bestScore: ', newScore, ', trial is: ', i, ', text is: ', transform_text(input_string, bestKey, original_letters))
        elif newScore == bestScore:
            if randrange(0,2) == 1:
                letters = new_letters[:]
                print('New bestScore: ', newScore, ', trial is: ', i, ', text is: ', transform_text(input_string, letters, original_letters))
    return bestKey

def swap(letters, letters_count):
    i = randrange(0, letters_count)
    j = randrange(0, letters_count)
    if i == j:
        swap(letters, letters_count)
    letters[i], letters[j] = letters[j], letters[i]
    return letters

def score(new_letters, input_string, matrix):
    original_letters = get_letters()
    candidate = transform_text(input_string, new_letters, original_letters)

    showed_pairs = set()

    scr = 0
    candidate_len = len(candidate)

    for (i, letter) in enumerate(candidate):
        index_first = original_letters.index(letter)
        if i != (candidate_len - 1):
            index_next = original_letters.index(candidate[i+1])
            pair = letter + candidate[i+1]
            if pair not in showed_pairs:
                showed_pairs.add(pair)
                scr += candidate.count(pair) * matrix[index_first][index_next]

    return scr

def transform_text(cipherText, key, original_letters):
    new_text = ''
    for letter in cipherText:
        new_text += original_letters[key.index(letter)]
    return new_text

def main_func(input_string, letters, letters_count, max_trials, max_swaps, matrix):
    new_letters = decode(input_string, letters, letters_count, max_trials, max_swaps, matrix)
    return transform_text(input_string, new_letters, letters)

if __name__ == "__main__":
    start_time = time.time()
    letters = get_letters()
    letters_count = len(letters)
    max_trials = get_max_trials()
    max_swaps = get_max_swaps()
    matrix = open_matrix()

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for thread in range(max_threads):
            futures.append(executor.submit(main_func, input_string, letters, letters_count, max_trials, max_swaps, matrix))

        for future in futures:
            print(future.result())
    
    finish_time = time.time()
    print(finish_time - start_time)