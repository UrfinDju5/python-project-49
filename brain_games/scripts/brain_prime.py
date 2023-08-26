from brain_games import games_logic
from brain_games.games.game_prime import MESAGE_START
from brain_games.games.game_prime import generate_random_example


def main():
    games_logic.run_game(generate_random_example, MESAGE_START)


if __name__ == "__main__":
    main()
