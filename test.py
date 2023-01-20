from character import Character
from fight import Fight
from cli import CLI
from skills import *

# TESTING


# Create Characters __init__(name='player', hp=20, spd=5, is_player=False, skills=[])
char1 = Character("Billy", 20, 5, True, [Uppercut(), ThroatPunch()])
char2 = Character("Johnny", 20, 3, True, [RoundhouseKick(), SuperSlap(), TestSkill()])
char3 = Character("Clarence", 12, 6, False, [ThroatPunch(), RoundhouseKick()])
char4 = Character("Tina", 12, 5, False, [PutridFlatulant(), SuperSlap()])
char5 = Character("Jimbo", 12, 4, False, [SuperSlap(), Uppercut()])

# Create Teams
player_team = [char1, char2]
enemy_team = [char3, char4, char5]

cli = CLI()
game = Fight(player_team, enemy_team, cli)


if __name__ == "__main__":
    game.fight()