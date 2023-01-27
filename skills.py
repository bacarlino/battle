

class Skill:
    # def __init__(self, name, desc, sp, dmg, cd, targets=1):
    #     self.name = name
    #     self.desc = desc
    #     self.sp = sp
    #     self.dmg = dmg
    #     self.cd = cd
    #     self.targets = targets

    def __str__(self):
        return f"{self.sp} SP | {self.name}"

    def reduce_cooldown(self, amount):
        self.cd -= amount

    def reset_cooldown(self):
        self.cd = self.init_cd


# class TestSkill(Skill):
#     def __init__(self):
#         super().__init__(
#             "Test Skill",
#             "A skill just used for testing...that's all",
#             5,
#             9999,
#             5,
#             1
#         )


# class AnotherSkill(Skill):
#     def __init__(self):
#         super().__init__(
#             "Another Test Skill",
#             "Another skill made just for testing",
#             5,
#             4732432748392748329,
#             5,
#             0
#         )


class PutridFlatulant(Skill):
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 5
    dmg = 10
    init_cd = 3
    cd = init_cd
    targets = 0



class RoundhouseKick(Skill):
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 5
    dmg = 10
    init_cd = 3
    cd = init_cd


class ThroatPunch(Skill):
    name = "Throat Punch"
    desc = "A quick sharp jab right to the jugular"
    sp = 5
    dmg = 10
    init_cd = 3
    cd = init_cd


class Uppercut(Skill):
    name = "Uppercut"
    desc = "A massive sweeping blow to the chin"
    sp = 5
    dmg = 10
    init_cd = 3
    cd = init_cd

class SuperSlap(Skill):
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 5
    dmg = 10
    init_cd = 3
    cd = init_cd