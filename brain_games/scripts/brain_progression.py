#!/usr/bin/env python3
from brain_games.games.game_progression import MESAGE_START
from brain_games import games_logic
from brain_games.games.game_progression import generate_random_example


def main():
    games_logic.run_game(generate_random_example, MESAGE_START)


if __name__ == "__main__":
    main()
