from random import randint


DESCRIPTION_GAME = 'Find the greatest common divisor of given numbers.'
MINIMUM_GENERATED_NUMBER = 1
MAXIMUM_GENERATED_NUMBER = 100


def generate_random_question():
    number1 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    number2 = randint(MINIMUM_GENERATED_NUMBER, MAXIMUM_GENERATED_NUMBER)
    random_example = [number1, number2]
    right_answer = str(determining_correct_answer(random_example))
    question = str(number1), str(number2)
    question = ' '.join(question)
    question = 'Question: ' + question
    return (question, right_answer)


def determining_correct_answer(random_example):
    random_example.sort()
    min_num, max_num = random_example
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
