#!/usr/bin/env python3
from brain_games import games_logic
from brain_games.games.calculation_game import generate_random_example
from brain_games.games.calculation_game import MESAGE_START


def main():
    games_logic.run_game(generate_random_example, MESAGE_START)


if __name__ == "__main__":
    main()
