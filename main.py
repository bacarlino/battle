import battle
import enemies
import factories
from battle_cli import BattleCLI

ENEMY_TYPES = [
    enemies.Rat,
    enemies.Bat,
    enemies.Spider,
    enemies.Skeleton,
    enemies.Zombie,
    enemies.Goon
]


def main():
    cli = BattleCLI()
    team1 = factories.build_team(2, is_player=True)
    team2 = factories.build_enemy_team(ENEMY_TYPES, 5)


    while True:
        restart = battle.Battle(team1, team2, cli).run()
        if restart:
            continue
        else:
            break
        
if __name__ == "__main__":
    main()