import status

class Item:
    status = None
    
    def __init__(self, qty=1):
        self.qty = qty
    
    def __str__(self) -> str:
        return f"{self.name}{' '*(15-len(self.name))}| {self.description}"
    
    def add_qty(self, qty):
        self.qty += qty
    
    def rm_qty(self, qty):
        self.qty -= qty 
        if self.qty < 0:
            self.qty = 0

class HealHPItem(Item):
    type = "heal"
    stat = "hp"


class GiveSPItem(Item):
    type = "heal"
    stat = "sp"

class DamageHPItem(Item):
    type = "damage"
    stat = "hp"

class BuffItem(Item):
    type = "buff"

class DebuffItem(Item):
    type = "debuff"

class Bandage(HealHPItem):
    name = "Bandage"
    amount = 6
    description = "A basic bandage that heals 6 HP"

class Knife(DamageHPItem):
    name = "Knife"
    status = status.Bleeding
    type = "damage"
    amount = 8
    description = "A sharp knife that deals 8 damage"

class PepperSpray(DebuffItem):
    name = "Pepper Spray"
    status = status.Blind
    amount = 0
    description = "A stinging spray that causes blindness impacting accuracy"

class EnergyDrink(BuffItem):
    name = "Energy Drink"
    status = status.Amped
    amount = 0
    description = "A boosting drink that grants an extra turn"
