from enum import Enum
import utilities


class Status(Enum):
    DEFENDING = "defending"
    UNCONCIOUS = "unconcious"
    BLIND = "blind"
    AMPED = "amped"
    POISONED = "poisoned"

    def __str__(self):
        return self.value

    def cap(self):
        return self.value.capitalize()


class StatusEffect:
    
    def __init__(self, duration):
        self.duration = duration

    def decrease_duration(self, amount):
        self.duration -= amount

    def increase_duration(self, amount):
        self.duration += amount


class Blind(StatusEffect):
    name = "Blind"
    description = "can't see shit"

    def __init__(self, duration=1):
        super().__init__(duration)

class Unconcious(StatusEffect):
    name = "Unconcious"
    description = "Lose a turn during the next round"
    
    def __init__(self, duration=1):
        super().__init__(duration)

class Amped(StatusEffect):
    name = "Amped"
    duration = 1
    description = "Gain an extra turn during the next round"

    def __init__(self, duration=1):
        super().__init__(duration)