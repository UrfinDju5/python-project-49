from brain_games import greeting
from brain_games import games_logic
from brain_games.games import game_prime


def main():
    name = greeting.welcome_user()
    games_logic.game_logic('prime', game_prime.MESAGE_START, name)


if __name__ == "__main__":
    main()
