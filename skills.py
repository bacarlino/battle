

class Skill:
    def __init__(self, name, desc, sp, dmg, cd, targets=1):
        self.name = name
        self.desc = desc
        self.sp = sp
        self.dmg = dmg
        self.cd = cd
        self.targets = targets


class TestSkill(Skill):
    def __init__(self):
        super().__init__(
            "Test Skill",
            "A skill just used for testing...that's all",
            5,
            9999,
            5,
            1
        )


class PutridFlatulant:
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 5
    dmg = 10
    cd = 5


class RoundhouseKick:
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 5
    dmg = 10
    cd = 5


class ThroatPunch:
    name = "Throat Punch"
    desc = "A quick sharp jab right to the jugular"
    sp = 5
    dmg = 10
    cd = 5


class Uppercut:
    name = "Uppercut"
    desc = "A massive sweeping blow to the chin"
    sp = 5
    dmg = 10
    cd = 5


class SuperSlap:
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 5
    dmg = 10
    cd = 5