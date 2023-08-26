from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'Find the greatest common divisor of given numbers.'


def generate_random_example():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    random_example = number1, number2
    sorted_example = sort_randome_example(random_example)
    right_answer = right_decision(sorted_example)
    return [random_example, right_answer]


def sort_randome_example(random_example):
    number1, number2 = random_example
    if number1 < number2:
        min_num, max_num = number1, number2
    else:
        min_num, max_num = number2, number1
    return [min_num, max_num]


def right_decision(sorted_example):
    min_num, max_num = sorted_example
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
