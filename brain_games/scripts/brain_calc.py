#!/usr/bin/env python3
from brain_games import greeting
from brain_games import games_logic
from brain_games.games import calculation_game


def main():
    name = greeting.welcome_user()
    games_logic.game_logic('calc', calculation_game.MESAGE_START, name)


if __name__ == "__main__":
    main()
