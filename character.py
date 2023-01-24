import random
from utilities import *
from items import Item


class Character:
    """Characters for player and enemies"""
    def __init__(self, name='player', hp=20, spd=5, is_player=False, skills=[]):      
        self.name = name
        self.hp = hp
        self.sp = 10
        self.atk = 5
        self.accuracy = .05
        self.speed = spd
        self.actions = [self.attack, self.defend, self.use_skill]
        self.skills = skills
        self.is_player = is_player
        self.is_defending = False
        self.active = True
        self.items = []

    def __str__(self):
        return (
            f"{self.name}{' '*(10-len(self.name))}|"
            f"{' '*(4-len(str(self.hp)))} {self.hp} HP |"
            f"{' '*(4-len(str(self.sp)))}{self.sp} SP | "
            f"{yellow('Defending' if self.is_defending else '')}"
        )

    def __repr__(self):
        return f"Character(name={self.name}, hp={self.hp}, sp={self.sp})"

    def attack(self):
        crit = False
        adj = int(self.atk * 0.25)
        dmg = random.randint(self.atk - adj, self.atk + adj)
        if random.random() > 0.9:
            crit = True
            dmg = self.atk * 2
        return dmg, crit

    def take_damage(self, amt):
        if self.is_defending:
            amt = int(amt / 2)
        result = self.hp - amt
        if result <= 0:
            self.hp = 0
        else:
            self.hp = result
        
    def defend(self):
        self.is_defending = True
    
    def stop_defending(self):
        self.is_defending = False

    def can_use_skill(self, skill):
        return self.sp >= skill.sp

    def use_skill(self, skill):
        self.sp -= skill.sp

    def heal(self, amount):
        self.hp += amount

    def is_dead(self):
        return self.hp <= 0

    def add_item(self, item: Item) -> None:
        self.items.append(item)
    
    def remove_item(self, item: Item) -> None:
        self.items.remove(item)

    def use_item(self, item: Item, target) -> None:
        item.use(target)


class Team:
    """Not implemented"""
    def __init__(self, members: list[Character]):
        self.full_team = members
        self.active_team = members
        self.inactive_team = []

    def get_active_team(self) -> list[Character]:
        return self.active_team

    def add_member(self, member) -> None:
        self.full_team.append(member)
        self.active_team.append(member)
    
    def remove_member(self, member) -> None:
        self.full_team.remove(member)
    
    def set_active(self, member) -> None:
        pass



