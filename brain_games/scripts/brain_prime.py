from brain_games import games_logic
from brain_games.games.prime_game import DESCRIPTION_GAME
from brain_games.games.prime_game import generate_random_question


def main():
    games_logic.run_game(generate_random_question, DESCRIPTION_GAME)


if __name__ == "__main__":
    main()
