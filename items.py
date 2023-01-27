import status

class Item:

    def __str__(self) -> str:
        return self.name


class HealHPItem(Item):
    type = "heal"
    stat = "hp"


class GiveSPItem(Item):
    type = "heal"
    stat = "sp"


class DamageHPItem(Item):
    type = "damage"
    stat = "hp"


class DebuffItem(Item):
    type = "debuff"


class Bandage(HealHPItem):
    name = "Bandage"
    amount = 6
    description = "A basic bandage that heals 6 HP"


class Knife(DamageHPItem):
    name = "Knife"
    type = "damage"
    amount = 8
    description = "A sharp knife that deals 8 damage"

    def use(self, target):
        target.take_damage(self.amount)


class PepperSpray(DebuffItem):
    name = "Pepper Spray"
    status = status.Blind
    description = "Burns eyes"

 