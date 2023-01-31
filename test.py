import character
from character import Character
from battle import Fight
from battle_cli import BattleCLI
from skills import *
import team


def main():
    cli = BattleCLI()
    team1 = team.build_team(10, is_player=True)
    team2 = team.build_team(10)

    while True:
        restart = Fight(team1, team2, cli).fight()
        if restart:
            continue
        else:
            break

if __name__ == "__main__":
    main()