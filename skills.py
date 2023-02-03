import random

DMG_RANGE = 0.25

class Skill:
    dmg_all = False
    status = None

    def __str__(self) -> str:
        return f"{self.name}{' '*(20-len(self.name))}| {self.sp} SP | "

    def rand_damage(self) -> int:
        adjusted = self.dmg * DMG_RANGE
        return int(random.randrange(self.dmg - adjusted, self.dmg + adjusted ))
        
    def hits_all(self):
        return self.dmg_all


class PutridFlatulant(Skill):
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 4
    dmg = 10
    dmg_all = True
    status = "poison"


class RoundhouseKick(Skill):
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 5
    dmg = 12


class ThroatPunch(Skill):
    name = "Throat Punch"
    desc = "A quick sharp jab right to the jugular"
    sp = 3
    dmg = 8


class Uppercut(Skill):
    name = "Uppercut"
    desc = "A massive sweeping blow to the chin"
    sp = 4
    dmg = 10


class SuperSlap(Skill):
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 3
    dmg = 8


class NeckBite(Skill):
    """Bat"""
    name = "NeckBite"
    desc = "Two fangs deep into the flesh"
    sp = 2
    dmg = 2
    status = "bleed"


class GuanoBath(Skill):
    """Bat"""
    name = "Guano Bath"
    des = "A smelly spray of wet bat shit"
    sp = 2
    dmg = 2
    dmg_all = True
    status = "poison"


