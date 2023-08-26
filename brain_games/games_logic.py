from brain_games import greeting


NUMBER_OF_GAME_REPETITIONS = 3
MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'


def ask_user_question(func):
    question, right_answer = func()
    print('Question: ', end='')
    print(*question)
    user_answer = input('Your answer: ')
    try:
        user_answer = int(user_answer)
    except ValueError:
        return user_answer, right_answer
    return user_answer, right_answer


def response_definition(func):
    user_answer, right_answer = ask_user_question(func)
    if user_answer == right_answer:
        return 'Correct!'
    else:
        return f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'."


def run_game(func, mesage_start):
    name = greeting.welcome_user()
    print(mesage_start)
    i = 0
    while i < NUMBER_OF_GAME_REPETITIONS:
        result_game = response_definition(func)
        if result_game == 'Correct!':
            print(result_game)
            i += 1
        else:
            return print(f"{result_game}\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')
