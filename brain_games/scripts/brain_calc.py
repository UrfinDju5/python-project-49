#!/usr/bin/env python3
from brain_games import games_logic
from brain_games.games.calculation_game import generate_random_question
from brain_games.games.calculation_game import DESCRIPTION_GAME


def main():
    games_logic.run_game(generate_random_question, DESCRIPTION_GAME)


if __name__ == "__main__":
    main()
