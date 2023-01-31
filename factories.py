import random

import character
import items
import skills
import team

def create_char(is_player=False):
    if is_player:
        hp = random.randint(18,22)
        speed = random.randint(20, 100)
        is_player = True
    else:
        hp = random.randint(12, 15)
        speed = random.randint(1, 80)

    sp = random.randint(8,12)
    name = random.choice([
    "Davey", "Diane", "Duane", "Edward", "Susi", "Trish", "Bobby", "Frank", "Woim",
    "Louis", "Roxanne", "Madd", "Mitch", "Butch", "Mark", "Mike", "Tim", "Tony", 
    "Chad", "Karen", "Stan", "Sanders", "Billy", "Johnny"
    ])
    skill_list = random.sample([
        skills.PutridFlatulant(),
        skills.RoundhouseKick(),
        skills.SuperSlap(),
        skills.ThroatPunch(),
        skills.Uppercut()
    ], k=2
    )

    item_list = random.sample([
        items.Bandage(),
        items.Knife(),
        items.PepperSpray(),
        items.EnergyDrink()
    ], k=2
    )
    return character.Character(name=name, hp=hp, sp=sp, speed=speed, skills=skill_list, items = item_list, is_player=is_player)


def build_team(size=2, is_player=False):
    team_list = []
    used_names = []
    new_char = create_char(is_player)
    used_names.append(new_char.name)

    while len(team) < size:
        new_char = create_char(is_player)
        if new_char.name not in used_names:
            team_list.append(new_char)
            used_names.append(new_char.name)

    return team.Team(team)

