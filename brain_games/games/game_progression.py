from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'What number is missing in the progression?'


def generate_random_example():
    start = randint(2, 20)
    step = randint(2, 7)
    stop = start + step * 10
    progression = list(range(start, stop, step))
    unknown_element = randint(0, 9)
    right_answer = progression.pop(unknown_element)
    progression.insert(unknown_element, '..')
    return progression, right_answer


def user_decision(progression):
    print('Question: ', end='')
    print(*progression)
    user_answer = input('Your answer: ')
    try:
        user_answer = int(user_answer)
    except ValueError:
        return user_answer
    return user_answer


def verdict():
    progression, right_answer = generate_random_example()
    user_answer = user_decision(progression)
    if user_answer == right_answer:
        return 'Correct!'
    else:
        return f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'."
