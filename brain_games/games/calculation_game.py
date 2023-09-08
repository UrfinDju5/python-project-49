from random import randint, choice


DESCRIPTION_GAME = 'What is the result of the expression?'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 50
MATH_SYMBOLS = ('+', '-', '*')


def generate_random_question():
    number1 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    number2 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    symbol = choice(MATH_SYMBOLS)
    right_answer = str(calculate_right_answer(number1, symbol, number2))
    question = f'Question: {str(number1)} {symbol} {str(number2)}'
    return (question, right_answer)


def calculate_right_answer(number1, symbol, number2):
    match symbol:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
