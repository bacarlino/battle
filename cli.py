import time
from utilities import *

T = 1

def line():
        print('----------------------------------------------')


class CLI:

    def press_enter_pause(self):
        input(f"Press {blue('ENTER / RETURN')} to continue")
        print()

    def enemy_turn_pause(self):
        input(f"Enemy Turn - Press {blue('ENTER / RETURN')} to continue")
        print()

    def display_invalid_command(self):
        print("Huh? That's not a valid command. Try again...")

    def display_title(self):
        line()
        print()
        print(f"A {red('FIGHT')} has started!")
        print()
        self.press_enter_pause()

    def display_all_fighters(self, player_team, fighter, enemy_team):
        # line()
        print()
        print(green('Your Team'))
        #time.sleep(T)
        for player in player_team:
            if player == fighter:
                print(f"{green(player.__str__())}")
            else:
                if player.is_dead():
                    print(f"{black(player)}")
                else:
                    print(f"{white(player)}")
                
        time.sleep(T)
        print()
        print(red('Your Enemies'))
        #time.sleep(T)
        for enemy in enemy_team:
            if enemy == fighter:
                print(f"{red(enemy.__str__())}")
            else:
                if enemy.is_dead():
                    print(f"{black(enemy)}")
                else:
                    print(f"{white(enemy)}")
        print()
        time.sleep(T)

    def display_fighters_turn(self, name, is_player, round):
        line()
        if is_player:
            print(f"Round {round} - {green(name)}'s Turn")
        else:
            print(f"Round {round} - {red(name)}'s Turn")
        #line()
        time.sleep(T)

    def display_options(self):
        print('+------------------------------------------+')
        print(f'| {red("(A)ttack")} | {yellow("(D)efend")} | {magenta("(S)kill)")} | {cyan("(I)tem)")} |')
        print('+------------------------------------------+')
        #time.sleep(T)
    
    def get_option(self, name):
        print("Your Turn - Type a LETTER then press ENTER")
        print()
        time.sleep(T)
        choice = input(f'{green(name)}: ')
        return choice

    def display_action(self, symbol):
        time.sleep(.5)
        print(symbol)
        time.sleep(.5)
        print(symbol*2)
        time.sleep(.5)
        print(symbol*3)
        time.sleep(.5)

    def choose_attack_target(self, enemy_team):
        line()
        print(f"Who do you want to {red('attack?')}")
        print()
        time.sleep(T)
        valid = []
        for num, enemy in enumerate(enemy_team):
            valid.append(str(num+1))
            print(f"({num+1}) {enemy}")
        print()
        while True:
            target = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
            if target in valid:
                return target
            else:
                print("Who? Try again...")
        

    def display_attack(self, attacker, defender, amt, is_crit):
        line()
        print(f"{attacker.name} is attacking {defender.name}")
        self.display_action(".")
        if is_crit:
            self.display_crit()
        print(f"{defender.name} takes {amt} damage")
        time.sleep(1.5)

    def display_crit(self):
        print("BOOM! A critical hit!")
        time.sleep(T)

    def display_defend(self, defender):
        line()
        print(f"{defender.name} takes a defensive stance")

    def choose_skill(self, skills):
        while True:
            try:
                line()
                print("Which skill do you want to use?")
                print()
                time.sleep(T)
                for num, skill in enumerate(skills):
                    print(f"({num+1}) {skill.name}{' '*(18-len(skill.name))}| {skill.sp} SP |")
                print()
                time.sleep(T)
                input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
                line()
                if 0 < int(input_num) <= len(skills):
                    return skills[int(input_num)-1]
                else:
                    print("What skill? Try again...")
            except ValueError:
                print("That's not a number. Try again...")

    def choose_skill_target(self, skill: str, enemy_team: list):
        while True:
            try:
                print(f"Who do you want to use {magenta(skill)} on?")
                print()
                for num, enemy in enumerate(enemy_team):
                    print(f"({num+1}) {enemy}")
                print()
                time.sleep(T)
                input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
                print()
                if 0 < int(input_num) <= len(enemy_team):
                    return enemy_team[int(input_num)-1]
                else:
                    print("Who? Try again...")
            except ValueError:
                print("That's not a number. Try again...")

    def display_skill_fail(self, name, sp):
        line()
        print(f"{name} doesn't have {sp} SP")

    def display_use_skill(self, attacker, skill, defender, dmg):
        line()
        print(f"{attacker} uses {skill.name} on {defender} and delivers {skill.desc.lower()}")
        self.display_action("*")
        print(f"{defender} takes {dmg} damage")

    def display_fighter_died(self, fighter):
        print(f"{fighter} is dead!")

    def display_player_loss(self):
        time.sleep(1)
        line()
        print("Your team's been wiped out. you LOSE!")
    
    def display_enemy_loss(self):
        time.sleep(1)
        line()
        print("The enemy has been annihilated. You WIN!")

    def display_game_over(self):
        line()
        print("GAME OVER")
        line()

