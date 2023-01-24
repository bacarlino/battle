

class Item:
    
    def use(self):
        pass


class Potion:
    name = "Potion"
    type = "heal"
    amount = 6
    description = "A healing potion that restores 6 HP"

    def use(self, target):
        target.heal(self.amount)


class Knife:
    name = "Knife"
    type = "damage"
    amount = 8
    description = "A sharp knife that deals 8 damage"

    def use(self, target):
        target.take_damage(self.amount)

