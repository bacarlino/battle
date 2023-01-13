import time
import random


def line():
        print('-------------------------------------------------------')
        


class Character:
    def __init__(self, name='player', spd=5, is_player=False):      
        self.name = name
        self.hp = 50
        self.sp = 20
        self.atk = 5
        self.speed = spd
        self.actions = [self.attack, self.defend, self.use_skill]
        self.is_player = is_player
        self.is_defending = False

    def __str__(self):
        return f'{self.name} - {self.hp} HP / {self.sp} SP'

    def __repr__(self):
        return f'Character(name={self.name}, hp={self.hp}, sp={self.sp})'

    def attack(self, defender):
        print(f"{self.name} is attacking {defender.name}")
        dmg = int(random.uniform(self.atk - self.atk*0.25, self.atk + self.atk*0.25))
        return dmg

    def take_damage(self, amt):
        print(f"{self.name} takes {amt} damage")
        self.hp -= amt

    def defend(self):
        print(f"{self.name} defends")
        self.is_defending = True

    def use_skill(self, skill):
        # skill should have a name, description, and damage amount
        print("Using a skill")


class Skill:

    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

class DragonsBreath(Skill):

    def __init__(self):
        super().__init__(self)


class Fight:

    def __init__(self, player_team, enemies):
        self.player_team = player_team
        self.enemies = enemies
        self.all_participants = player_team + enemies
        self.turn_order=[]
 
    def display_title(self):
        line()
        print("A FIGHT HAS STARTED!")
    
    
    def display_fighters(self):
        line()
        print('YOUR TEAM')
        for player in self.player_team:
            print(f"- {player}")
        print()
        print('ENEMY TEAM')
        for enemy in self.enemies:
            print(f"- {enemy}")

    
    def display_options(self):
        line()      
        print('Your choices:')
        print()
        print('(A)ttack | (D)efend | (S)kill | (I)tem | (R)un')
        print()

    def set_turn_order(self):
        self.all_participants.sort(key=lambda player: player.speed)

    def proc_choice(self, player_char, choice):
        line()
        """Process user input"""
        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:

            print("Who do you want to attack?")
            print()
            options = enumerate(self.enemies)
            for num, enemy in enumerate(self.enemies):
                print(f"{num+1} - {enemy}")
            print()
            target = input("Type a number: ")

            self.handle_attack(player_char, self.enemies[int(target)-1])
            
        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            print("DEFENDING!")
            self.handle_defend(player_char)

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            print("USING A SKILL!")

        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            print("USING AN ITEM!")

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")
        
        else:
            print("HUH?")


    def handle_attack(self, attacker, defender):

        line()
        amt = attacker.attack(defender)
        if defender.is_defending:
            amt = int(amt / 2)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        defender.take_damage(amt)

    def handle_defend(self, defender):
        line()
        defender.defend()

    def handle_skill(self, user):
        pass

    def handle_ai(self, fighter):
        action = random.choice(fighter.actions)
        target = random.choice(self.player_team)

        if action == fighter.attack:
            self.handle_attack(fighter, target)
        if action == fighter.defend:
            self.handle_defend(fighter)
        




    def player_turn(self):
        pass
    
    def enemy_turn(self):
        pass

    def fight(self):
        """
        This function controls the fight itself.
        
        During players turn:
            Display list of options

        """

        self.display_title()

        # GAME LOOP
        while True:
            
            # Display fighters and determine turn order based on character speed stat
            #self.display_fighters()
            self.set_turn_order()

            # Iterate through the turn order list
            for fighter in self.all_participants:
                self.display_fighters()
                time.sleep(1.5)
                line()
                print(f"~~ It's {fighter.name}'s turn ~~")
                time.sleep(1.5)
                # If it's a player character's turn, display their options for that character
                if fighter.is_player:
                    fighter.is_defending = False
                    # Display our options, ask for input, and process the input
                    self.display_options()
                    choice = input('Type a command and press ENTER: ')
                    self.proc_choice(fighter, choice)
                else:
                    # AI should decide what to do and to which player character
                    # Dumb AI to choose actions and targets at random
                    self.handle_ai(fighter)
                    
                    # Smart AI to determine actions and targets conditionally
                time.sleep(1.5)



# TESTING

# Create Characters
char1 = Character("Billy", 5, True)
char2 = Character("Johnny", 3, True)
char3 = Character("Clarence", 6)
char4 = Character("Tina", 5)
char5 = Character("Jimbo", 4)

# Create Teams
player_team = [char1, char2]
enemies = [char3, char4, char5]

game = Fight(player_team, enemies)


if __name__ == "__main__":
    game.fight()