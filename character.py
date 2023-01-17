import random


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
        self.dead = False

    def __str__(self):
        return (
            f"{self.name}{' '*(10-len(self.name))}| {self.hp} HP | {self.sp} SP | "
            f"{'Defending' if self.is_defending else ''}"
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
            amt = amt / 2
        result = self.hp - amt
        if result <= 0:
            self.hp = 0
            self.dead = True
        else:
            self.hp = result
        
    def defend(self):
        self.is_defending = True

    def use_skill(self, skill):
        self.sp -= skill.sp


class Team:
    """Not implemented"""
    def __init__(self, members=[]):
        self.members = []