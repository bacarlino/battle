import time
import random


def line():
        print('----------------------------------------------')


class Character:
    def __init__(self, name='player', spd=5, is_player=False, skills=[]):      
        self.name = name
        self.hp = 20
        self.sp = 10
        self.atk = 5
        self.speed = spd
        self.actions = [self.attack, self.defend, self.use_skill]
        self.skills = skills
        self.is_player = is_player
        self.is_defending = False
        self.dead = False

    def __str__(self):
        return f"{self.name}{' '*(10-len(self.name))}| {self.hp} HP | {self.sp} SP |"

    def __repr__(self):
        return f"Character(name={self.name}, hp={self.hp}, sp={self.sp})"

    def attack(self):
        dmg = int(random.uniform(self.atk - self.atk*0.25, self.atk + self.atk*0.25))
        return dmg

    def take_damage(self, amt):
        result = self.hp - amt
        if result <= 0:
            self.hp = 0
            self.dead = True
        else:
            self.hp = result
        
    def defend(self):
        print(f"{self.name} defends")
        self.is_defending = True

    def use_skill(self, skill):
        self.sp -= skill.sp


class PutridFlatulant:
    name = "Putrid Flatulant"
    desc = "A thick green cloud of skin melting filth"
    sp = 5
    dmg = 10
    cd = 5

class RoundhouseKick:
    name = "Roundhouse Kick"
    desc = "A powerful spinning kick to the face"
    sp = 5
    dmg = 10
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
    sp = 5
    dmg = 10
    cd = 5

class SuperSlap:
    name = "Super Slap"
    desc = "A wide swinging open palm slap to the face"
    sp = 5
    dmg = 10
    cd = 5


class Fight:

    def __init__(self, player_team, enemies):
        self.player_team = player_team
        self.enemies = enemies
        self.all_participants = []
        self.turn_order=[]
 
    def display_title(self):
        line()
        print("A FIGHT HAS STARTED!")
        print()
        input("Press ENTER/RETURN to start")
    
    
    def display_fighters(self):
        time.sleep(1)
        line()
        print('<<< YOUR TEAM >>>')
        time.sleep(1)
        for player in self.player_team:
            print(f"{player}")
        time.sleep(1)
        print()
        print('<<< ENEMY TEAM >>>')
        time.sleep(1)
        for enemy in self.enemies:
            print(f"{enemy}")
        time.sleep(1)        

    def display_options(self, fighter):
        #line()
        # print(f"Your options for {fighter.name}:")
        # time.sleep(.5)
        # print()      
        print('(A)ttack  (D)efend  (S)kill')
        time.sleep(.5)
        print()
        choice = input('Type a command (or letter) and press ENTER: ')
        self.proc_choice(fighter, choice)

    def set_turn_order(self):
        self.all_participants = self.player_team + self.enemies
        self.all_participants.sort(key=lambda player: player.speed)
        

    def proc_choice(self, player, choice):
        line()
        """Process user input"""
        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:

            print("Who do you want to attack?")
            time.sleep(1)
            print()
            valid = []
            for num, enemy in enumerate(self.enemies):
                valid.append(str(num+1))
                print(f"({num+1}) {enemy}")
            print()
            
            while True:
                time.sleep(1)
                target = input("Type a number: ")
                if target in valid:
                    self.handle_attack(player, self.enemies[int(target)-1])
                    break
                else:
                    print("Who? Try again...")

        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            self.handle_defend(player)

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            print("Which skill do you want to use?")
            print()
            time.sleep(.5)
            valid = []
            for num, skill in enumerate(player.skills):
                valid.append(str(num+1))
                print(f"({num+1}) {skill.name}{' '*(18-len(skill.name))}| {skill.sp} SP |")
            print()

            while True:
                time.sleep(.5)
                input_num = input("Type a number: ")
                if input_num in valid:
                    skill = player.skills[int(input_num)-1]

                    if player.sp >= skill.sp:
                        time.sleep(.5)
                        line()
                        print(f"Who do you want to use {skill.name} on?")
                        print()
                        valid = []
                        for num, enemy in enumerate(self.enemies):
                            valid.append(str(num+1))
                            print(f"({num+1}){enemy}")
                        print()
                    
                        while True:
                            target = input("Type a number: ")
                            if target in valid:
                                defender = self.enemies[int(target)-1]
                                self.handle_skill(player, skill, defender)
                                break
                            else:
                                print("Who? Try again...")
                    else:
                        line()
                        print(f"{player.name} doesn't have {skill.sp} SP")
                        self.display_options(player)
                    break
                else:
                    print("What skill? Try again....")


        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            print("USING AN ITEM!")

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")
        
        else:
            print("Huh? That's not a valid command... try again.")
            self.display_options(player)


    def handle_attack(self, attacker, defender):
        
        amt = attacker.attack()
        if defender.is_defending:
            amt = int(amt / 2)
        defender.take_damage(amt)

        line()
        print(f"{attacker.name} is attacking {defender.name}")
        time.sleep(0.75)
        print(".")
        time.sleep(0.75)
        print(".")
        time.sleep(0.75)
        print(".")
        time.sleep(0.75)
        print(f"{defender.name} takes {amt} damage")
        if defender.dead:
            line()
            print(f"{defender.name} is dead!")

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
            print(f"{user.name} uses {skill.name} on {defender.name} and delivers {skill.desc.lower()}")
            time.sleep(0.75)  
            print("*")
            time.sleep(0.75)
            print("*")
            time.sleep(0.75)
            print("*")
            time.sleep(0.75)
            print(f"{defender.name} takes {dmg} damage")
            if defender.dead:
                line()
                print(f"{defender.name} is dead!")
        else:
            print(f"{user.name} doesn't have {skill.sp} SP")
            self.handle_ai(user)

    def handle_ai(self, fighter):

        avail_target = [target for target in self.player_team if not target.dead]
        action = random.choice(fighter.actions)
        target = random.choice(avail_target)
        skill = random.choice(fighter.skills)

        if action == fighter.attack:
            self.handle_attack(fighter, target)
        if action == fighter.defend:
            self.handle_defend(fighter)
        if action == fighter.use_skill:
            self.handle_skill(fighter, skill, target)

    def fight(self):
        """This function controls the fight itself."""
        
        endgame = False
        self.display_title()

        # GAME LOOP
        round = 1
        while True:
            line()
            print(f"ROUND {round}")
            self.set_turn_order()
            
            for fighter in self.all_participants:
                if not fighter.dead:
                    self.display_fighters()
                    line()
                    print(f"~~ It's {fighter.name}'s turn ~~")
                    line()
                    time.sleep(1)

                    if fighter.is_player:
                        fighter.is_defending = False
                        self.display_options(fighter)
                    else:
                        input("Press ENTER/RETURN to continue")
                        self.handle_ai(fighter)
                
                player_deaths = 0
                enemy_deaths = 0
                for player in self.player_team:
                    if player.dead:
                        player_deaths += 1
                for enemy in self.enemies:
                    if enemy.dead:
                        enemy_deaths += 1
                
                if player_deaths == len(self.player_team):
                    time.sleep(1)
                    line()
                    print("Your entire team is dead. GAME OVER. You LOSE!")
                    line()
                    endgame = True
                    break
                if enemy_deaths == len(self.enemies):
                    time.sleep(1)
                    line()
                    print("The enemy team is dead. You WIN!")
                    (line)
                    endgame = True
                    break
                
            if endgame:
                break    
            round += 1




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