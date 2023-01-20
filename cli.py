import time

def line():
        print('----------------------------------------------')

class CLI:

    def press_enter_pause(self):
        input("Press ENTER / RETURN to continue")

    def display_invalid_command(self):
        print("Huh? That's not a valid command. Try again...")

    def display_title(self):
        line()
        print("A FIGHT HAS STARTED!")
        print()
        self.press_enter_pause()

    def display_round_num(self, round):
        line()
        print(f"ROUND {round}")

    def display_all_fighters(self, player_team, enemy_team):
        time.sleep(1)
        line()
        print('<<< YOUR TEAM >>>')
        time.sleep(1)
        for player in player_team:
            print(f"{player}")
        time.sleep(1)
        print()
        print('<<< ENEMY TEAM >>>')
        time.sleep(1)
        for enemy in enemy_team:
            print(f"{enemy}")
        time.sleep(1)

    def display_fighters_turn(self, name):
        line()
        print(f"~~ It's {name}'s turn ~~")
        line()
        time.sleep(1)

    def display_options(self):
        print('(A)ttack  (D)efend  (S)kill')
        time.sleep(1)
        print()
        choice = input('Type a command (or letter) and press ENTER: ')
        return choice

    def display_action(self, symbol):
        time.sleep(0.5)
        print(symbol)
        time.sleep(0.5)
        print(symbol*2)
        time.sleep(0.5)
        print(symbol*3)
        time.sleep(0.5)

    def choose_attack_target(self, enemy_team):
        line()
        print("Who do you want to attack?")
        time.sleep(1)
        print()
        valid = []
        for num, enemy in enumerate(enemy_team):
            valid.append(str(num+1))
            print(f"({num+1}) {enemy}")
        print()
        while True:
            time.sleep(1)
            target = input("Type a number: ")
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

    def display_crit():
        print("BOOM! A critical hit!")
        time.sleep(0.5)

    def display_defend(self, defender):
        line()
        print(f"{defender.name} takes a defensive stance")

    def choose_skill(self, skills):
        while True:
            try:
                line()
                print("Which skill do you want to use?")
                print()
                time.sleep(.5)
                for num, skill in enumerate(skills):
                    print(f"({num+1}) {skill.name}{' '*(18-len(skill.name))}| {skill.sp} SP |")
                print()
                time.sleep(.5)
                input_num = input("Type a number: ")
                if 0 < int(input_num) < len(skills)+1:
                    return skills[int(input_num)-1]
                else:
                    print("What skill? Try again...")
            except ValueError:
                print("That's not a number. Try again...")

    def choose_skill_target(self, skill: str, enemy_team: list):
        while True:
            try:
                print(f"Who do you want to use {skill} on?")
                print()
                for num, enemy in enumerate(enemy_team):
                    print(f"({num+1}) {enemy}")
                print()
                time.sleep(.5)
                input_num = input("Type a number: ")
                if 0 < int(input_num) < len(enemy_team):
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

