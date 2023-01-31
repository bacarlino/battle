from dataclasses import dataclass

import character as char

class Enemy(char.Character):

    def __init__(self, name, hp, speed, skills, items):
        sp = 0
        super().__init__(self, name, hp, sp, speed, skills, items)
        self.actions = ["attack", "defend", "skill"]


class Bat(Enemy):

    def __init__():
        super().__init__(
            self,
            name="Bat",
            hp = (2,6),
            speed = (1, 100),
            skills = [],
            items = []
        )

@dataclass
class TestBat(Enemy):
    name: str = "Test Bat"
    hp: tuple = 5
    speed: tuple = 50




