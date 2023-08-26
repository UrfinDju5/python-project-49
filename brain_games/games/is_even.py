from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_example():
    random_number = randint(1, 100)
    right_decision = is_right_answer(random_number)
    return [[random_number], right_decision]


def is_right_answer(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
