from dataclasses import dataclass

import character as char
from utilities import *



class Enemy(char.Character):

    def __init__(self, name, hp, atk):
        sp = 0
        super().__init__(name, hp, sp, atk)
        self.actions = ["attack", "defend", "skill"]

    def __str__(self):
        statuses = ""
        for status in self.statuses:
            if status.type == "buff":
                statuses += green(status.name + " ")
            else:
                statuses += red(status.name + " ")
        return (
            f"{self.name}{' '*(10-len(self.name))}|"
            f"{' '*(3-len(str(self.hp)))} {self.hp}/{self.max_hp}{' '*(2-len(str(self.max_hp)))} HP |"
            f"{yellow('Defending ' if self.defending else '')}" + statuses
        )

    def has_skills(self):
        print(self.skills)
        return len(self.skills) > 0

class Rat(Enemy):

    def __init__(self):
        super().__init__(
            name="Big Rat",
            hp = 4,
            atk=2
        )


class Spider(Enemy):

    def __init__(self):
        super().__init__(
            name="Spider",
            hp = 6,
            atk=3
        )


class Bat(Enemy):

    def __init__(self):
        super().__init__(
            name="Bat",
            hp = 8,
            atk = 4
        )


class Skeleton(Enemy):

    def __init__(self):
        super().__init__(
            name="Skeleton",
            hp = 10,
            atk = 5
        )


class Zombie(Enemy):

    def __init__(self):
        super().__init__(
            name="Zombie",
            hp = 12,
            atk = 6
        )


class Goon(Enemy):

    def __init__(self):
        super().__init__(
            name = "Goon",
            hp = 15,
            atk = 7
        )


if __name__ == "__main__":
    g = Goon()
    print(g.name, g.hp, g.atk)
    print(g.attack())