from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_example():
    random_number = randint(1, 100)
    return random_number


def right_decision(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def user_decision(random_number):
    print(f'Question: {random_number}')
    user_answer = input('Your answer: ')
    return user_answer


def verdict():
    random_number = generate_random_example()
    right_answer = right_decision(random_number)
    user_answer = user_decision(random_number)
    if user_answer == right_answer:
        return 'Correct!'
    else:
        return f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'."
