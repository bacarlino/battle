

class Skill:
    
    def __str__(self):
        return f"{self.name}{' '*(20-len(self.name))}| {self.sp} SP | "

    def reduce_cooldown(self, amount):
        self.cd -= amount

    def reset_cooldown(self):
        self.cd = self.init_cd


class PutridFlatulant(Skill):
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 4
    dmg = 10
    init_cd = 3
    cd = init_cd
    targets = 0


class RoundhouseKick(Skill):
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 5
    dmg = 12
    init_cd = 3
    cd = init_cd


class ThroatPunch(Skill):
    name = "Throat Punch"
    desc = "A quick sharp jab right to the jugular"
    sp = 3
    dmg = 8
    init_cd = 3
    cd = init_cd


class Uppercut(Skill):
    name = "Uppercut"
    desc = "A massive sweeping blow to the chin"
    sp = 4
    dmg = 10
    init_cd = 3
    cd = init_cd


class SuperSlap(Skill):
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 3
    dmg = 8
    init_cd = 3
    cd = init_cd