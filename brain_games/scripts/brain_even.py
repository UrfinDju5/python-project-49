#!/usr/bin/env python3
from brain_games import greeting
from brain_games.games import is_even
from brain_games import games_logic


def main():
    greeting.welcome_user()
    name = greeting.name
    games_logic.game_logic('even', is_even.MESAGE_START, name)


if __name__ == "__main__":
    main()
