from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'Answer "yes" if given number is prime. Otherwise answer "no".'
SIMPLE_NUMBER = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
    173, 179, 181, 191, 193, 197, 199
]


def generate_random_example():
    random_number = randint(1, 200)
    right_answer = right_decision(random_number)
    return [[random_number], right_answer]


def right_decision(random_number):
    if random_number in SIMPLE_NUMBER:
        return 'yes'
    else:
        return 'no'
