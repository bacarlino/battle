from character import Character
from fight import Fight
from skills import *

# TESTING

# Create Characters __init__(name='player', hp=20, spd=5, is_player=False, skills=[])
char1 = Character("Billy", 22, 5, True, [Uppercut(), ThroatPunch()])
char2 = Character("Johnny", 18, 3, True, [RoundhouseKick(), SuperSlap(), TestSkill()])
char3 = Character("Clarence", 10, 6, False, [ThroatPunch()])
char4 = Character("Tina", 8, 5, False, [PutridFlatulant()])
char5 = Character("Jimbo", 12, 4, False, [SuperSlap()])

# Create Teams
player_team = [char1, char2]
enemy_team = [char3, char4, char5]

game = Fight(player_team, enemy_team)


if __name__ == "__main__":
    game.fight()