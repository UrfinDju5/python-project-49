from random import randint


DESCRIPTION_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 50


def generate_random_question():
    random_number = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    question = f'Question: {str(random_number)}'
    return (question, right_answer)
