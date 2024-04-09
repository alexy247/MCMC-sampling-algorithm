import os
from utils import get_letters, get_max_trials, get_max_swaps, open_matrix, transform_text, score
from random import shuffle, randrange
from concurrent.futures import ThreadPoolExecutor
import time

max_threads = 2 * os.cpu_count()

# input_string = "щдшэсздбгдтиылъирдвсдпирвясндждягфгдогъзд бгдсынъьисздегясздргсдовяг биъьисзднтдбнёдщдыифвсиадшсвдсвдтиыифислоиадмвжэмиадориъгаджижд бгдмыгъясиорщрвяздбгжвсвывцдявфясогббвясзадндодыгтэрзсисгддвънбдшг въибдмыншг дъвоврзбвдяжыв бвхвдыит гыидолёвънсдщдбнюнцджиждпгдусвдмврэшнрвяз"
# кошка сдохла мл мсфзолбдс
# милый друг олкецщйцуд
input_string = "ояилюцвгуэ"

def decode_with_max_swaps(input_string, original_letters, letters_count, max_trials, max_swaps, matrix):
    letters = original_letters.copy()
    print('letters: ', letters)

    bestSwap = 0
    bestKey = letters.copy()
    bestScore = score(bestKey, input_string, matrix)
    print('bestKey: ', bestKey)
    print('bestScore: ', bestScore)

    shuffle(letters)
    print('shuffle letters: ', letters)

    for i in range(0, max_trials):
        shuffle(letters)
        bestTrialScore = 0
        for j in range(0, max_swaps):
            new_letters = swap(letters.copy(), letters_count)
            newScore = score(new_letters, input_string, matrix)
            if newScore > bestTrialScore:
                letters = new_letters.copy()
                bestTrialScore = newScore
                bestSwap = j
            elif newScore == bestTrialScore:
                if randrange(0,2) == 1:
                    letters = new_letters.copy()
        if bestTrialScore > bestScore:
            bestKey = letters.copy()
            bestScore = bestTrialScore
            print('New bestScore: ', bestTrialScore, ', trial is: ', i, 'swap is: ', bestSwap, ', text: ', transform_text(input_string, bestKey, original_letters))
    return bestKey

def swap(letters, letters_count):
    new_letters = []
    i = randrange(0, letters_count)
    j = randrange(0, letters_count)
    if i == j:
        swap(letters, letters_count)
    letters[i], letters[j] = letters[j], letters[i]
    new_letters = letters.copy()
    return new_letters

def main_func(input_string, letters, letters_count, max_trials, max_swaps, matrix):
    new_letters = decode_with_max_swaps(input_string, letters, letters_count, max_trials, max_swaps, matrix)
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

    # print(transform_text('текст', ['т', 'е', 'к', 'с'], ['м', 'е', 'к', 'с']))
    # print(swap(letters.copy(), letters_count))