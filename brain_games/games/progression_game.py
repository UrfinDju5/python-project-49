from random import randint


DESCRIPTION_GAME = 'What number is missing in the progression?'
MINIMUM_GENERATED_NUMBER = 2
MAXIMUM_GENERATED_NUMBER = 20
MINIMUM_GENERATED_STEP = 2
MAXIMUM_GENERATED_STEP = 7
LEN_PROGRESSION = 10
MIN_INDEX_UNKNOWN_ELEMENT = 0


def generate_random_question():
    start = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    step = randint(MINIMUM_GENERATED_STEP, MAXIMUM_GENERATED_STEP)
    stop = start + step * LEN_PROGRESSION
    progression = list(range(start, stop, step))
    unknown_element = randint(MIN_INDEX_UNKNOWN_ELEMENT, len(progression) - 1)
    right_answer = str(progression[unknown_element])
    progression[unknown_element] = '..'
    question = f"Question: {''.join(f'{str(i)} ' for i in progression)}"
    return (question, right_answer)
