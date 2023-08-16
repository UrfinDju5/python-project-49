#!/usr/bin/env python3
from brain_games import greeting
from brain_games.games import game_progression
from brain_games import games_logic


def main():
    name = greeting.welcome_user()
    games_logic.game_logic('progression', game_progression.MESAGE_START, name)


if __name__ == "__main__":
    main()
