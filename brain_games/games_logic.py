from brain_games import greeting
import prompt


NUMBER_OF_GAME_REPETITIONS = 3
MESAGE_WRONG = 'is wrong answer ;(. Correct answer was'


def ask_user_question(generate_random_question):
    question, right_answer = generate_random_question()
    print(question)
    user_answer = prompt.string('Your answer: ')
    return user_answer, right_answer


def run_game(generate_random_question, description_game):
    name = greeting.welcome_user()
    print(description_game)
    for _ in range(NUMBER_OF_GAME_REPETITIONS):
        user_answer, right_answer = ask_user_question(generate_random_question)
        if user_answer != right_answer:
            return print(
                f"'{user_answer}' {MESAGE_WRONG} '{right_answer}'.\
                \nLet's try again, {name}!")
        print('Correct!')
    print(f'Congratulations, {name}!')
