import random
from utilities import *
from items import Item


class StatusEffect:
    
    def __init__(self, duration):
        self.duration = duration

    def decrease_duration(self, amount):
        self.duration -= amount

    def increase_duration(self, amount):
        self.duration += amount


class Blinded(StatusEffect):
    name = "Blinded"
    description = "Significantly decreased accuracy"

    def __init__(self, duration=1):
        super().__init__(duration)

class Unconcious(StatusEffect):
    name = "Unconcious"
    description = "Lose a turn during the next round"
    
    def __init__(self, duration=1):
        super().__init__(duration)

class Amped(StatusEffect):
    name = "Amped"
    duration = 1
    description = "Gain an extra turn during the next round"

    def __init__(self, duration=1):
        super().__init__(duration)


class Character:
    def __init__(self, name='Player', hp=20, spd=5, skills=[], is_player=False):      
        self.name = name
        self.hp = hp
        self.sp = 10
        self.atk = 5
        self.accuracy = .05
        self.speed = spd
        self.skills = skills
        self.defending = False
        self.items = []
        self.statuses = []
        self.active = True
        self.actions = ["attack", "defend", "skill"]
        self.is_player = is_player

    def __str__(self):
        return (
            f"{self.name}{' '*(10-len(self.name))}|"
            f"{' '*(4-len(str(self.hp)))} {self.hp} HP |"
            f"{' '*(4-len(str(self.sp)))}{self.sp} SP | "
            f"{yellow('Defending ' if self.defending else '')}"
            f"{red('Blinded ') if 'Blinded' in self.statuses else ''}"
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
        result = self.hp - amt
        if result <= 0:
            self.hp = 0
        else:
            self.hp = result
        
    def defend(self):
        self.defending = True
    
    def stop_defending(self):
        self.defending = False

    def can_use_skill(self, skill):
        return self.sp >= skill.sp

    def use_skill(self, skill):
        self.sp -= skill.sp

    def add_hp(self, amount):
        self.hp += amount

    def is_dead(self):
        return self.hp <= 0

    def add_item(self, item: Item):
        self.items.append(item)
    
    def remove_item(self, item: Item):
        self.items.remove(item)

    def add_status(self, status):
        self.statuses.append(status)
        print("TESTING: ADDED STATUS")

    def turn_refresh(self):
        """Reset defending status, reduce skill cooldowns and status durations"""
        if self.defending:
            self.stop_defending()
        for skill in self.skills:
            skill.reduce_cooldown(1)
        for status in self.statuses:
            status.decrease_duration(1)



# class Team:
#     """Not implemented"""
#     def __init__(self, members: list[Character]):
#         self.full_team = members
#         self.active_team = members
#         self.inactive_team = []

#     def get_active_team(self) -> list[Character]:
#         return self.active_team

#     def add_member(self, member) -> None:
#         self.full_team.append(member)
#         self.active_team.append(member)
    
#     def remove_member(self, member) -> None:
#         self.full_team.remove(member)
    
#     def set_active(self, member) -> None:
#         pass



