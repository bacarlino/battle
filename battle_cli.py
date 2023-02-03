import time
from utilities import *

T = .5

def line():
        print('----------------------------------------------')


class BattleCLI:

    def press_enter_pause(self):
        input(f"Press {blue('ENTER / RETURN')} to continue")
        print()

    def enemy_turn_pause(self):
        print()
        input(f"Enemy Turn - Press {blue('ENTER / RETURN')} to continue")

    def display_invalid_command(self):
        print("That's not an option. Try again...")

    def display_title(self):
        print(
            red('''

 (        (                      )               
 )\ )     )\ )     (          ( /(          )    
 /(_))    /(_))   (()/(      ((_)\     ( )(_))   
(_))_|   (_))      /(_))_     _((_)   (_(_())    
| |_     |_ _|    (_)) __|   | || |   |_   _|    
| __|     | |       | (_ |   | __ |     | |      
|_|      |___|       \___|   |_||_|     |_|      
                                                '''
        ))
        # time.sleep(1)

    def display_instructions(self):
        print(
            f"- {red('Defeat')} all of the enemies by reducing their HP (hit points) to 0 \n"
            f"- {magenta('Skills')} use SP (skill points) and do more damage\n"
            f"- {cyan('Items')} can be used for various effects\n"
            f"- {yellow('Defend')} to reduce incoming damage"
            )
        print()
        # time.sleep(1)

    def display_help(self):
        line()
        print()
        self.display_instructions()
        self.press_enter_pause()

    def display_all_fighters(self, player_team, fighter, enemy_team):
        # line()
        print()
        print(green('         -- Your Team --'))
        time.sleep(.05)
        for player in player_team:
            if player == fighter:
                print(f"{yellow(player.__str__())}")
            else:
                if player.is_dead():
                    print(f"{black(player)}")
                else:
                    print(f"{white(player)}")
            time.sleep(.05)

        time.sleep(T)
        print()
        print(red("        -- Your Enemies --"))
        time.sleep(.1)
        for enemy in enemy_team:
            if enemy == fighter:
                print(f"{yellow(enemy.__str__())}")
            else:
                if enemy.is_dead():
                    print(f"{black(enemy)}")
                else:
                    print(f"{white(enemy)}")
            
            time.sleep(.1)
        print()
        time.sleep(T)

    # def display_team(self, team):
    #     for char in team:
    #         if char == fighter:
    #             print(f"{red(char.__str__())}")
    #         else:

    #             if char.is_dead():
    #                 print(f"{black(char)}")
    #             else:
    #                 print(f"{white(char)}")

    def display_fighters_turn(self, name, round):
        line()
        print(f"Round {round} - {name}'s Turn")
        time.sleep(T)

    def display_options(self):
        print(f"+-----------------------------------------+ {black('---(H)elp')}")
        print(f"| {red('(A)ttack')} | {magenta('(S)kill')} | {cyan('(I)tem)')} | {green('(D)efend')} | {black('---(O)ptions')}")
        print(f"+-----------------------------------------+ {black('---(R)estart')}")
        # time.sleep(T)
    
    def get_main_option(self, name):
        print("===========================================")
        print(f"YOUR TURN - Type a {blue('LETTER')} then press {blue('ENTER')}")
        print()
        choice = input(f'{yellow(name)} => ')
        return choice

    def display_action(self, symbol):
        time.sleep(.25)
        print(symbol)
        time.sleep(.25)
        print(symbol*2)
        time.sleep(.25)
        print(symbol*3)
        time.sleep(.25)


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
                    time.sleep(.1)
                print()
                print(f"{blue(num+2)} | CANCEL")
                time.sleep(.1)

                print()
                time.sleep(T)
                input_num = input(f"Type a {blue('NUMBER')} then press {blue('ENTER')}: ")
                if 0 < int(input_num) <= len(choices):
                    return choices[int(input_num)-1]
                elif int(input_num) == len(choices)+1:
                    return None
                else:
                    print("That's not a choice. Try again...")
                    time.sleep(T)
            except ValueError:
                print("That's not a number. Try again...")

    def cancel_choice(self):
        line()
        print("Canceled")
        line()
        time.sleep(T)

    def display_attack(self, attacker, defender, amt, is_crit):
        line()
        print(f"{attacker.name} is attacking {defender.name}")
        self.display_action(".")
        if is_crit:
            self.display_crit()
        print(f"{defender.name} takes {amt} damage")
        time.sleep(2)

    def display_crit(self):
        print("BOOM! A critical hit!")
        time.sleep(T)

    def display_miss(self, name):
        line()
        print(f"{name} misses")
        time.sleep(T)

    def display_defend(self, defender):
        line()
        print(f"{defender.name} {yellow('defends')}")
        time.sleep(2)

    def display_skill_fail(self, name, sp):
        line()
        print(f"{name} doesn't have {sp} SP")
        time.sleep(2)

    def display_use_skill(self, attacker, skill, defender, dmg):
        line()
        print(f"{attacker} uses {skill.name} on {defender} and delivers {skill.desc.lower()}")
        time.sleep(1.5)
        self.display_action("*")
        print(f"{defender} takes {dmg} damage")
        time.sleep(2)

    def display_use_item(self, item_user, item, item_target):
        line()
        print(f"{item_user} uses {item} on {item_target}")
        self.display_action("$")
      
    def display_heal(self, target, amount):
        print(f"{target} restores {amount} HP")
        time.sleep(2)
    
    def display_take_damage(self, name, amount, cause=False):
        if cause:
            print(f"{name} {cause} and takes {amount} damage")
        else:
            print(f"{name} takes {amount} damage")
        time.sleep(2)

    def display_lost_turn(self, character, status):
        print(f"{character} {status.verb} and lost their turn")
        time.sleep(2)

    def display_add_status(self, target, status_verb):
        print(f"{target} {status_verb}")
        time.sleep(2)
    
    def display_amped_effect(self, char):
        print(f"{char} is Amped and takes an extra turn this round")

    def display_unconcious_effedt(self, char):
        print(f"{char} is Unconcious and loses their turn")

    def display_no_items(self, item_user):
        line()
        print(f"{item_user} doesn't have any items to use")
        time.sleep(2)
    
    def display_fighter_died(self, fighter):
        print(f"{fighter} is dead!")
        time.sleep(2)

    def display_player_loss(self):
        time.sleep(1)
        line()
        print("Your team's been wiped out. you LOSE!")
        time.sleep(2)
    
    def display_enemy_loss(self):
        time.sleep(1)
        line()
        print("The enemy has been annihilated. You WIN!")
        time.sleep(2)

    def display_game_over(self):
        line()
        print("GAME OVER")
        line()

