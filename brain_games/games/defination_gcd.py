from random import randint


MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'
MESAGE_START = 'Find the greatest common divisor of given numbers.'


def generate_random_example():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    return [number1, number2]


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


def user_decision(random_example):
    number1, number2 = random_example
    print('Question: ', end='')
    print(number1, number2)
    user_answer = input('Your answer: ')
    try:
        user_answer = int(user_answer)
    except ValueError:
        return user_answer
    return user_answer


def verdict():
    random_example = generate_random_example()
    right_answer = right_decision(sort_randome_example(random_example))
    user_answer = user_decision(random_example)
    if user_answer == right_answer:
        return 'Correct!'
    else:
        return f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'."
