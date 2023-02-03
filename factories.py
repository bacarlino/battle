import random

import character
import enemies
import items
import skills
import team



CHARTYPES = {
    "rat": enemies.Rat,
    "spider": enemies.Spider,
    "bat": enemies.Bat,
    "skeleton": enemies.Skeleton,
    "zombie": enemies.Zombie,
    "goon": enemies.Goon
}

def create_char(is_player):
    if is_player:
        hp = random.randint(18,22)
        speed = random.randint(30, 100)
        is_player = True
        atk = 5
    else:
        hp = random.randint(4,6)
        speed = random.randint(1,70)

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
    return character.Character(name=name, hp=hp, sp=sp, atk=atk, speed=speed, skills=skill_list, items = item_list, is_player=is_player)


def build_team(size=2, is_player=False):
    team_list = []
    used_names = []
    new_char = create_char(is_player)
    used_names.append(new_char.name)

    while len(team_list) < size:
        new_char = create_char(is_player)
        if new_char.name not in used_names:
            team_list.append(new_char)
            used_names.append(new_char.name)

    return team.Team(team_list)






def create_enemy(chartype):
    return CHARTYPES[chartype]()

def build_enemy_team(typeslist, size):
    teamlist = []
    while len(teamlist) < size:
         teamlist.append(random.choice(typeslist)())
    return team.Team(teamlist)

if __name__ == "__main__":
    print(build_enemy_team([enemies.Bat, enemies.Skeleton, enemies.Rat], 5))