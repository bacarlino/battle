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

    def display_invalid_command(self):
        print("That's not an option. Try again...")

    def display_title(self):
        #line()
        # print()
        # print(f"A {red('FIGHT')} has started!")
        print(
            '''

 (        (                      )               
 )\ )     )\ )     (          ( /(          )    
 /(_))    /(_))   (()/(      ((_)\     ( )(_))   
(_))_|   (_))      /(_))_     _((_)   (_(_())    
| |_     |_ _|    (_)) __|   | || |   |_   _|    
| __|     | |       | (_ |   | __ |     | |      
|_|      |___|       \___|   |_||_|     |_|      
                                                '''
        )

    def display_instructions(self):
        print(
            "Instructions:\n"
            f"- {red('Defeat')} all of the enemies by reducing their HP (hit points) to 0 \n"
            f"- {yellow('Defend')} to reduce incoming damage\n"
            f"- {magenta('Skills')} use SP (skill points) and do more damage\n"
            f"- {cyan('Items')} can be used for various effects"
            )
        print()

    def display_all_fighters(self, player_team, fighter, enemy_team):
        line()
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
        print(red("Your Enemies"))
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

    def display_fighters_turn(self, name, round):
        
        print(f"Round {round} - {name}'s Turn")
        
        time.sleep(T)

    def display_options(self):
        print('+-----------------------------------------+')
        print(f'| {red("(A)ttack")} | {yellow("(D)efend")} | {magenta("(S)kill")} | {cyan("(I)tem)")} |')
        print('+-----------------------------------------+')
        time.sleep(T)
    
    def get_main_option(self, name):
        print("Your Turn - Type a LETTER then press ENTER")
        print()
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


    def choose(self, action, choices, named=None):

        prompts = {
            "attack": f"Who do you want to {red('attack?')}",
            "skill": f"Which {magenta('skill')} do you want to use?",
            "skill_target": f"Who do you want to use {magenta(named)} on?",
            "item": "Which item do you want to use?",
            "item_target": f"Who do you want to use {cyan(named)} on?"
        }

        while True:
            try:
                line()
                print(prompts[action])
                print()
                time.sleep(T)
                for num, option in enumerate(choices):
                    print(f"{blue(num+1)} | {option}")
                print()
                time.sleep(T)
                input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
                if 0 < int(input_num) <= len(choices):
                    return choices[int(input_num)-1]
                else:
                    print("That's not a choice. Try again...")
                    time.sleep(T)
            except ValueError:
                print("That's not a number. Try again...")

    # def choose_attack_target(self, enemy_team):
    #     while True:
    #         try:
    #             line()
    #             print(f"Who do you want to {red('attack?')}")
    #             print()
    #             time.sleep(T)
    #             for num, enemy in enumerate(enemy_team):
    #                 print(f"{blue(num+1)} | {enemy}")
    #             print()
    #             time.sleep(T)
    #             input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
    #             if 0 < int(input_num) <= len(enemy_team):
    #                 return enemy_team[int(input_num)-1]
    #             else:
    #                 print("Who? Try again...")
    #                 time.sleep(T)
    #         except ValueError:
    #             print("That's not a number. Try again...")

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
        print(f"{defender.name} {yellow('defends')}")
        time.sleep(1.5)

    # def choose_skill(self, skills):
    #     while True:
    #         try:
    #             line()
    #             print("Which skill do you want to use?")
    #             print()
    #             time.sleep(T)
    #             for num, skill in enumerate(skills):
    #                 print(f"{blue(num+1)} | {skill.name}{' '*(18-len(skill.name))}| {skill.sp} SP |")
    #             print()
    #             time.sleep(T)
    #             input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
    #             line()
    #             if 0 < int(input_num) <= len(skills):
    #                 return skills[int(input_num)-1]
    #             else:
    #                 print("What skill? Try again...")
    #         except ValueError:
    #             print("That's not a number. Try again...")

    # def choose_skill_target(self, skill: str, enemy_team: list):
    #     while True:
    #         try:
    #             print(f"Who do you want to use {magenta(skill)} on?")
    #             print()
    #             for num, enemy in enumerate(enemy_team):
    #                 print(f"({blue(num+1)}) {enemy}")
    #             print()
    #             time.sleep(T)
    #             input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
    #             if 0 < int(input_num) <= len(enemy_team):
    #                 return enemy_team[int(input_num)-1]
    #             else:
    #                 print("Who? Try again...")
    #         except ValueError:
    #             print("That's not a number. Try again...")

    def display_skill_fail(self, name, sp):
        line()
        print(f"{name} doesn't have {sp} SP")

    def display_use_skill(self, attacker, skill, defender, dmg):
        line()
        print(f"{attacker} uses {skill.name} on {defender} and delivers {skill.desc.lower()}")
        self.display_action("*")
        print(f"{defender} takes {dmg} damage")

    # def choose_item(self, items):
    #     while True:
    #         try:
    #             line()
    #             print("Which item do you want to use?")
    #             print()
    #             time.sleep(T)
    #             for num, item in enumerate(items):
    #                 print(f"{blue(num+1)} | {item.name}{' '*(18-len(item.name))}| {item.description}")
    #             print()
    #             time.sleep(T)
    #             input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
    #             line()
    #             if 0 < int(input_num) <= len(items):
    #                 return items[int(input_num)-1]
    #             else:
    #                 print("What item? Try again...")
    #         except ValueError:
    #             print("That's not a number. Try again...")

    # def choose_item_target(self, item: str, targets: list):
    #     while True:
    #         try:
    #             print(f"Who do you want to use {cyan(item)} on?")
    #             print()
    #             for num, target in enumerate(targets):
    #                 print(f"({blue(num+1)}) {target}")
    #             print()
    #             time.sleep(T)
                
    #             input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
    #             if 0 < int(input_num) <= len(targets):
    #                 return targets[int(input_num)-1]
    #             else:
    #                 print("Who? Try again...")
    #         except ValueError:
    #             print("That's not a number. Try again...")

    def display_use_item(self, item_user, item, item_target, amount):
        line()
        print(f"{item_user} uses {item.name} on {item_target}")
        self.display_action("$")
        if item.type == "damage":
            print(f"{item_target} takes {amount} damage")
        elif item.type == "heal":
            print(f"{item_target} restores {amount} HP")

    def display_heal(self, target, amount):
        print(f"{item_target} restores {amount} HP")
    
    def display_damage(self):
        pass

    def display_no_items(self):
        line()
        print(f"{fighter} doesn't have any items to use")
    
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

