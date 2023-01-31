import battle
import factories
from battle_cli import BattleCLI

def main():
    cli = BattleCLI()
    team1 = factories.build_team(2, is_player=True)
    team2 = factories.build_team(3)

    while True:
        restart = battle.Battle(team1, team2, cli).run()
        if restart:
            continue
        else:
            break
        
if __name__ == "__main__":
    main()