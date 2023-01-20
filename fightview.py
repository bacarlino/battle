import time

def line():
        print('----------------------------------------------')

def disp_action(symbol):
    time.sleep(0.5)
    print(symbol)
    time.sleep(0.5)
    print(symbol*2)
    time.sleep(0.5)
    print(symbol*3)
    time.sleep(0.5)

class FightView:

    def display_title(self):
        line()
        print("A FIGHT HAS STARTED!")
        print()
        input("Press ENTER/RETURN to start")

    def display_fighters(self, player_team, enemy_team):
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

    def display_options(self):
        """Displays main options for player characters and takes user input"""     
        print('(A)ttack  (D)efend  (S)kill')
        time.sleep(.5)
        print()
        choice = input('Type a command (or letter) and press ENTER: ')
        return choice
        #self.proc_choice(fighter, choice)        

    def display_action(symbol):
        time.sleep(0.5)
        print(symbol)
        time.sleep(0.5)
        print(symbol*2)
        time.sleep(0.5)
        print(symbol*3)
        time.sleep(0.5)

    def choose_attack_target(enemy_team):
        line()
        print("Who do you want to attack?")
        time.sleep(1)
        print()
        valid = []
        for num, enemy in enumerate(self.enemy_team):
            valid.append(str(num+1))
            print(f"({num+1}) {enemy}")
        print()
        