

class StatusEffect:
    amount = None
    verb = None
    
    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        return self.name

    def decrease_duration(self, amount):
        self.duration -= amount

    def increase_duration(self, amount):
        self.duration += amount


class BuffStat(StatusEffect):
    type = "buff"


class DebuffStat(StatusEffect):
    type = "debuff"


class Dead(StatusEffect):
    name = "Dead"
    description = ""
    verb = "has died"
    effect = "is dead"


class Amped(BuffStat):
    name = "Amped"
    description = "gains an extra turn next round"
    verb = "is amped up"

    def __init__(self):
        super().__init__(1)


class Blind(DebuffStat):
    name = "Blind"
    description = "can't see jack shit"
    verb = "is blinded"

    def __init__(self):
        super().__init__(2)


class Unconcious(DebuffStat):
    name = "Unconcious"
    description = "loses a turn"
    verb = "is unconcious"
    effect = "loses a turn"
    
    def __init__(self):
        super().__init__(1)


class Bleeding(DebuffStat):
    name = "Bleeding"
    description = "Lose HP at the start of turn"
    verb = "is bleeding"
    effect = "loses HP"

    def __init__(self):
        super().__init__(3)


class Poison(DebuffStat):
    name = "Poisened"
    description = "Lose HP and SP each turn"
    verb = "is poisened"
    effect = "loses HP and SP"
    amount = 2

    def __init_(self):
        super().__init__(3)
