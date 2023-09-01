from random import randint


DESCRIPTION_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_question():
    random_number = randint(1, 100)
    right_answer = str(determining_correct_answer(random_number))
    question = str(random_number)
    question = 'Question: ' + question
    return (question, right_answer)


def determining_correct_answer(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
