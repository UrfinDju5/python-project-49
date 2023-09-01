from random import randint, choice


DESCRIPTION_GAME = 'What is the result of the expression?'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 50
MATH_SYMBOLS = ('+', '-', '*')


def generate_random_question():
    number1 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    number2 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    symbol = choice(MATH_SYMBOLS)
    random_example = number1, symbol, number2
    right_answer = str(determining_correct_answer(random_example))
    question = str(number1), symbol, str(number2)
    question = ' '.join(question)
    question = 'Question: ' + question
    return (question, right_answer)


def determining_correct_answer(random_example):
    number1, symbol, number2 = random_example
    match symbol:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
