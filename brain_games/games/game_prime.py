from random import randint


DESCRIPTION_GAME = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 500


def generate_random_question():
    random_number = \
        randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    if is_prime(random_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = str(random_number)
    question = 'Question: ' + question
    return (question, right_answer)


def is_prime(num):
    if num < 2:
        return False
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k += 1
    if (k <= 0):
        return True
    else:
        return False
