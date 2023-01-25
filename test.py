from character import Character
from fight import Fight
from cli import CLI
from skills import *
import items


# TESTING

char1 = Character("Billy", 20, 5, [Uppercut(), ThroatPunch()], is_player=True)
char2 = Character("Johnny", 20, 3, [RoundhouseKick(), SuperSlap()], is_player=True)

char3 = Character("Clarence", 12, 6, [ThroatPunch(), RoundhouseKick()])
char4 = Character("Tina", 12, 5, [PutridFlatulant(), SuperSlap()])
char5 = Character("Jimbo", 12, 4, [SuperSlap(), Uppercut()])



# char1.add_skill([Uppercut(), ThroatPunch()]())
# char2.add_skill([SuperSlap(), RoundhouseKick()]())
# char3.add_skill([ThroatPunch(), RoundhouseKick()])
# char4.add_skill([PutridFlatulant(), SuperSlap()])
# char5.add_skill([SuperSlap(), Uppercut()])


char1.add_item(items.Knife())
char2.add_item(items.Knife())
char3.add_item(items.Knife())
char4.add_item(items.Knife())
char5.add_item(items.Knife())

char1.add_item(items.Bandage())
char2.add_item(items.Bandage())
# char2.add_item(items.PepperSpray())


player_team = [char1, char2]
enemy_team = [char3, char4, char5]



cli = CLI()
game = Fight(player_team, enemy_team, cli)


if __name__ == "__main__":
    game.fight()