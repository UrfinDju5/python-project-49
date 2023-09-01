from random import randint


DESCRIPTION_GAME = 'What number is missing in the progression?'


def generate_random_question():
    start = randint(2, 20)
    step = randint(2, 7)
    stop = start + step * 10
    progression = list(range(start, stop, step))
    unknown_element = randint(0, 9)
    right_answer = str(progression[unknown_element])
    progression[unknown_element] = '..'
    question = ''
    for i in progression:
        question += str(i) + ' '
    question = 'Question: ' + question
    return (question, right_answer)
