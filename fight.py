import time
import random
import os


class Fight:

    def __init__(self, player_team, enemy_team, cli):
        self.cli = cli
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.all_participants = []
        self.turn_order=[]

    def proc_choice(self, player, choice):
        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:
            target = self.cli.choose_attack_target(self.enemy_team)
            self.handle_attack(player, self.enemy_team[int(target)-1])

        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            self.handle_defend(player)

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            skill = self.cli.choose_skill(player.skills)
            if player.can_use_skill(skill):
                target = self.cli.choose_skill_target(skill.name, self.enemy_team)
                self.handle_skill(player, skill, target)
            else:
                self.cli.display_skill_fail(player.name, skill.sp)
                self.cli.display_options()
            
        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            print("USING AN ITEM!")

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")
        
        else:
            self.cli.display_invalid_command()
            self.display_options(player)


    def handle_attack(self, attacker, defender): 
        amt, is_crit = attacker.attack()
        defender.take_damage(amt)
        self.cli.display_attack(attacker, defender, amt, is_crit)
        if defender.is_dead():
            self.cli.display_fighter_died(defender.name)

    def handle_defend(self, defender):
        defender.defend()
        self.cli.display_defend(defender)

    def handle_skill(self, attacker, skill, defender):
        dmg = skill.dmg
        adj = dmg*0.25
        dmg = int(random.uniform(dmg - adj, dmg + adj))
        if defender.is_defending:
            dmg = int(dmg / 2)
        attacker.use_skill(skill)
        defender.take_damage(dmg)
        self.cli.display_use_skill(attacker.name, skill, defender.name, dmg)
        if defender.is_dead():
            self.cli.display_fighter_died(defender.name)
        

    def handle_ai(self, fighter):
        avail_target = [target for target in self.player_team if not target.is_dead()]
        action = random.choice(fighter.actions)
        target = random.choice(avail_target)
        skill = random.choice(fighter.skills)

        if action == fighter.attack:
            self.handle_attack(fighter, target)
        if action == fighter.defend:
            self.handle_defend(fighter)
        if action == fighter.use_skill:
            if fighter.can_use_skill(skill):
                self.handle_skill(fighter, skill, target)
            else:
                self.handle_ai(fighter)

    def set_turn_order(self):
        self.all_participants = self.player_team + self.enemy_team
        self.all_participants.sort(key=lambda player: player.speed)
    
    def clear_fighter_d(self, fighter):
        if fighter.is_defending:
            fighter.stop_defending()


    def fight(self):
        
        endgame = False
        round = 1

        self.cli.display_title()

        # MAIN BATTLE LOOP
        while True:
            # self.cli.display_round_num(round)
            self.set_turn_order()
            for fighter in self.all_participants:
                if not fighter.is_dead():
                    self.clear_fighter_d(fighter)
                    # os.system('clear')
                    self.cli.display_fighters_turn(fighter.name, fighter.is_player, round)
                    self.cli.display_all_fighters(self.player_team, fighter, self.enemy_team)
                    if fighter.is_player:
                        self.cli.display_options()
                        choice = self.cli.get_option(fighter.name)
                        self.proc_choice(fighter, choice)
                    else:
                        self.cli.enemy_turn_pause()
                        self.handle_ai(fighter)

                player_deaths = 0
                enemy_deaths = 0
                for player in self.player_team:
                    if player.is_dead():
                        player_deaths += 1
                for enemy in self.enemy_team:
                    if enemy.is_dead():
                        enemy_deaths += 1
                
                if player_deaths == len(self.player_team):
                    self.cli.display_player_loss()
                    endgame = True
                    break
                
                if enemy_deaths == len(self.enemy_team):
                    self.cli.display_enemy_loss()
                    endgame = True
                    break
                       
            if endgame:
                self.cli.display_game_over()
                break    
            round += 1
