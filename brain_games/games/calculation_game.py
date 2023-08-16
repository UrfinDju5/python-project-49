from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'What is the result of the expression?'


def generate_random_example():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    symbol = ['+', '-', '*'][randint(0, 2)]
    return [number1, symbol, number2]


def right_decision(random_example):
    number1, symbol, number2 = random_example
    match symbol:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2


def user_decision(random_example):
    number1, symbol, number2 = random_example
    print('Question: ', end='')
    print(number1, symbol, number2)
    user_answer = input('Your answer: ')
    try:
        user_answer = int(user_answer)
    except ValueError:
        return user_answer
    return user_answer


def verdict():
    random_example = generate_random_example()
    right_answer = right_decision(random_example)
    user_answer = user_decision(random_example)
    if user_answer == right_answer:
        return 'Correct!'
    else:
        return f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'."
