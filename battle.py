import time
import random


def line():
        print('----------------------------------------------')
        
class Character:
    def __init__(self, name='player', spd=5, is_player=False, skills=[]):      
        self.name = name
        self.hp = 20
        self.sp = 10
        self.atk = 100
        self.speed = spd
        self.actions = [self.attack, self.defend, self.use_skill]
        self.skills = skills
        self.is_player = is_player
        self.is_defending = False

    def __str__(self):
        return f'{self.name} - {self.hp} HP / {self.sp} SP'

    def __repr__(self):
        return f'Character(name={self.name}, hp={self.hp}, sp={self.sp})'

    def attack(self):
        dmg = int(random.uniform(self.atk - self.atk*0.25, self.atk + self.atk*0.25))
        return dmg

    def take_damage(self, amt):
        self.hp -= amt

    def defend(self):
        print(f"{self.name} defends")
        self.is_defending = True

    def use_skill(self, skill):
        self.sp -= skill.sp


class PutridFlatulant:
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 10
    dmg = 15
    cd = 5

class RoundhouseKick:
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 3
    dmg = 8
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
    sp = 7
    dmg = 12
    cd = 5

class SuperSlap:
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 4
    dmg = 9
    cd = 5

class Fight:

    def __init__(self, player_team, enemies):
        self.player_team = player_team
        self.enemies = enemies
        self.all_participants = player_team + enemies
        self.turn_order=[]
 
    def display_title(self):
        line()
        print("A FIGHT HAS STARTED!")
        input("Press ENTER to start")
    
    
    def display_fighters(self):
        line()
        print('YOUR TEAM')
        for player in self.player_team:
            print(f"- {player}")
        print()
        print('ENEMY TEAM')
        for enemy in self.enemies:
            print(f"- {enemy}")

    
    def display_options(self, fighter):
        line()      
        print(f"What does {fighter.name} do?")
        print()
        print('(A)ttack | (D)efend | (S)kill')
        print()
        choice = input('Type a command (or first letter) and press ENTER: ')
        self.proc_choice(fighter, choice)

    def set_turn_order(self):
        self.all_participants.sort(key=lambda player: player.speed)
        #random.choice(self.all_participants)

    def proc_choice(self, player, choice):
        line()
        """Process user input"""
        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:

            print("Who do you want to attack?")
            print()
            for num, enemy in enumerate(self.enemies):
                print(f"({num+1}) {enemy}")
            print()
            target = input("Type a number: ")
            self.handle_attack(player, self.enemies[int(target)-1])
            
        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            self.handle_defend(player)

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            print("Which skill do you want to use?")
            print()
            for num, skill in enumerate(player.skills):
                print(f"({num+1}) {skill.name} - {skill.sp} SP - {skill.desc}")
            print()
            input_num = input("Type a number: ")
            skill = player.skills[int(input_num)-1]

            if player.sp >= skill.sp:
                line()
                print(f"Who do you want to use {skill.name} on?")
                print()
                for num, enemy in enumerate(self.enemies):
                    print(f"({num+1}) - {enemy}")
                print()
                target = input("Type a number: ")
                defender = self.enemies[int(target)-1]
                self.handle_skill(player, skill, defender)

        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            print("USING AN ITEM!")

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")
        
        else:
            print("HUH?")


    def damage_exchange(self):
        pass 

    def handle_attack(self, attacker, defender):
        
        amt = attacker.attack()
        if defender.is_defending:
            amt = int(amt / 2)
        defender.take_damage(amt)

        line()
        print(f"{attacker.name} is attacking {defender.name}")  
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(f"{defender.name} takes {amt} damage")

    def handle_defend(self, defender):
        line()
        defender.defend()

    def handle_skill(self, user, skill, defender):

        if user.sp >= skill.sp:
            dmg = skill.dmg
            adj = dmg*0.25
            dmg = int(random.uniform(dmg - adj, dmg + adj))
            if defender.is_defending:
                dmg = int(dmg / 2)
            user.use_skill(skill)
            defender.take_damage(dmg)
            line()
            print(f"{user.name} uses {skill.name} and delivers {skill.desc.lower()} to {defender.name}")
            time.sleep(2)  
            print("*")
            time.sleep(0.75)
            print("*")
            time.sleep(0.75)
            print("*")
            time.sleep(0.75)
            print(f"{defender.name} takes {dmg} damage")
        else:
            print(f"{user.name} doesn't have {skill.sp} SP")

        

    def handle_ai(self, fighter):
        action = random.choice(fighter.actions)
        target = random.choice(self.player_team)
        skill = random.choice(fighter.skills)

        if action == fighter.attack:
            self.handle_attack(fighter, target)
        if action == fighter.defend:
            self.handle_defend(fighter)
        if action == fighter.use_skill:
            self.handle_skill(fighter, skill, target)

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
                time.sleep(2)
                line()
                print(f"~~ It's {fighter.name}'s turn ~~")
                time.sleep(2)
                # If it's a player character's turn, display their options for that character
                if fighter.is_player:
                    fighter.is_defending = False
                    # Display our options, ask for input, and process the input
                    self.display_options(fighter)
                    # choice = input('Type a command and press ENTER: ')
                    # self.proc_choice(fighter, choice)
                else:
                    # AI should decide what to do and to which player character
                    # Dumb AI to choose actions and targets at random
                    self.handle_ai(fighter)
                    
                    # Smart AI to determine actions and targets conditionally
                time.sleep(2)

# TESTING

# Create Characters __init__(name='player', spd=5, is_player=False, skills=[])
char1 = Character("Billy", 5, True, [Uppercut(), ThroatPunch()])
char2 = Character("Johnny", 3, True, [RoundhouseKick(), SuperSlap])
char3 = Character("Clarence", 6, False, [ThroatPunch()])
char4 = Character("Tina", 5, False, [PutridFlatulant()])
char5 = Character("Jimbo", 4, False, [SuperSlap()])

# Create Teams
player_team = [char1, char2]
enemies = [char3, char4, char5]

game = Fight(player_team, enemies)


if __name__ == "__main__":
    game.fight()