from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'What is the result of the expression?'


def generate_random_example():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    symbol = ['+', '-', '*'][randint(0, 2)]
    random_example = number1, symbol, number2
    right_answer = right_decision(random_example)
    return [random_example, right_answer]


def right_decision(random_example):
    number1, symbol, number2 = random_example
    match symbol:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
