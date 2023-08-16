from brain_games.games import is_even
from brain_games.games import calculation_game
from brain_games.games import defination_gcd
from brain_games import greeting
from brain_games.games import game_progression
from brain_games.games import game_prime


def game_logic(game_name, mesage_start, name):
    print(mesage_start)
    i = 0
    while i < 3:
        match game_name:
            case 'even':
                result_game = is_even.verdict()
            case 'calc':
                result_game = calculation_game.verdict()
            case 'gcd':
                result_game = defination_gcd.verdict()
            case 'progression':
                result_game = game_progression.verdict()
            case 'prime':
                result_game = game_prime.verdict()
        if result_game == 'Correct!':
            print(result_game)
            i += 1
        else:
            return print(f"{result_game}\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    name = greeting.welcome_user()
    game_logic('prime', game_prime.MESAGE_START, name)
