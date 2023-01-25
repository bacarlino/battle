

class Item:
    def __str__(self):
        return self.name


class Bandage(Item):
    name = "Bandage"
    type = "heal"
    amount = 6
    description = "A basic bandage that heals 6 HP"

    def use(self, target):
        target.heal(self.amount)


class Knife(Item):
    name = "Knife"
    type = "damage"
    amount = 8
    description = "A sharp knife that deals 8 damage"

    def use(self, target):
        target.take_damage(self.amount)


class PepperSpray(Item):
    name = "Pepper Spray"
    type = "status"
    effect = "blind"
    description = "Burns eyes"

 