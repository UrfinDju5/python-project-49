from random import randint


DESCRIPTION_GAME = 'Find the greatest common divisor of given numbers.'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 100


def generate_random_question():
    number1 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    number2 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    right_answer = str(get_gcd(number1, number2))
    question = f'Question: {str(number1)} {str(number2)}'
    return (question, right_answer)


def get_gcd(number1, number2):
    min_num = number1 if number1 < number2 else number2
    max_num = number1 if number1 > number2 else number2
    i = min_num
    result = min_num
    while i != 0:
        if max_num % i == 0:
            return result
        else:
            i = max_num % i
            max_num = min_num
            min_num = i
            result = i
