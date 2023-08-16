#!/usr/bin/env python3
from brain_games import greeting
from brain_games.games import defination_gcd
from brain_games import games_logic


def main():
    name = greeting.welcome_user()
    games_logic.game_logic('gcd', defination_gcd.MESAGE_START, name)


if __name__ == "__main__":
    main()
