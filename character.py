import random
import skills
import items
from utilities import *


class Character:
    def __init__(self, name, hp, sp, atk, speed=50, skills=[], items=[], is_player=False):      
        self.name = name
        self.max_hp = hp
        self.hp = hp 
        self.sp = sp
        self.atk = atk
        self.accuracy = .05
        self.speed = speed
        self.skills = skills
        self.defending = False
        self.items = items
        self.statuses = []
        # self.actions = ["attack", "defend", "skill"]
        self.is_player = is_player

    def __str__(self):
        statuses = ""
        for status in self.statuses:
            if status.type == "buff":
                statuses += green(status.name + " ")
            else:
                statuses += red(status.name + " ")
        return (
            f"{self.name}{' '*(10-len(self.name))}|"
            f"{' '*(3-len(str(self.hp)))} {self.hp}/{self.max_hp} HP |"
            f"{' '*(4-len(str(self.sp)))}{self.sp} SP | "
            f"{black('Dead' if self.is_dead() else '')}"
            f"{yellow('Defending ' if self.defending else '')}"
            + statuses
        )

    def __repr__(self):
        return f"Character(name={self.name}, hp={self.hp}, sp={self.sp})"

    def attack(self):
        crit = False        
        adj = int(self.atk * 0.25)
        dmg = random.randint(self.atk - adj, self.atk + adj)
        luck = random.random()
        if luck < 0.1 or "blind" in self.statuses:
            return None, False
        elif luck > 0.9:
            crit = True
            dmg = self.atk * 2
        return dmg, crit

    def take_damage(self, amt):
        result = self.hp - amt
        if result <= 0:
            self.hp = 0
            self.statuses = []
        else:
            self.hp = result
        
    def defend(self):
        self.defending = True

    def is_defending(self) -> bool:
        return self.defending
    
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

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def status_lst(self) -> list:
        return self.statuses

    def add_status(self, status):
        self.statuses.append(status())

    def remove_status(self, status):
        self.statuses.remove(status)

    def clear_all_statuses(self):
        self.statuses = []
            
    def update_statuses(self):
        for status in self.statuses:
            status.decrease_duration(1)
            if status.duration == 0:
                self.remove_status(status)
