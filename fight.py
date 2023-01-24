import time
import random
from character import Character



class Fight:

    def __init__(self, player_team, enemy_team, cli):
        self.cli = cli
        self.player_team = player_team
        self.enemy_team = enemy_team

    def get_avail_targets(self, team: list) -> list[Character]:
        return [target for target in team if not target.is_dead()]

    def handle_player_turn(self, fighter):
        while True:
            self.cli.display_options()
            choice = self.cli.get_option(fighter.name)
            self.proc_choice(fighter, choice)
            break

    def proc_choice(self, fighter, choice):
        avail_targets = self.get_avail_targets(self.enemy_team)

        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:
            target = self.cli.choose_attack_target(avail_targets)
            self.handle_attack(fighter, target)

        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            self.handle_defend(fighter)

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            skill = self.cli.choose_skill(fighter.skills)
            if fighter.can_use_skill(skill):
                target = self.cli.choose_skill_target(skill.name, avail_targets)
                self.handle_skill(fighter, skill, target)
            else:
                self.cli.display_skill_fail(fighter.name, skill.sp)
                self.cli.display_options()
            
        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            item = self.cli.choose_item(fighter.items)
            if item.type == "heal":
                avail_targets = self.get_avail_targets(self.player_team)
            target = self.cli.choose_item_target(item.name, avail_targets)
            self.handle_item(fighter, item, target)

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")
        
        else:
            self.cli.display_invalid_command()
            self.cli.display_options()


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

    def handle_item(self, item_user, item, item_target):
        amount = item.amount
        item_user.use_item(item, item_target)
        self.cli.display_use_item(item_user.name, item, item_target.name, amount)
        if item_target.is_dead():
            self.cli.display_fighter_died(item_target.name)

        
        

    def handle_ai_turn(self, fighter):
        avail_target = self.get_avail_targets(self.player_team)
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
        self.turn_order = self.player_team + self.enemy_team
        self.turn_order.sort(key=lambda player: player.speed)
    
    
    def clear_fighter_defense(self, fighter):
        if fighter.is_defending:
            fighter.stop_defending()


    def fight(self):
        
        endgame = False
        round = 1

        self.cli.display_title()
        self.cli.display_instructions()
        self.cli.press_enter_pause()

        # MAIN BATTLE LOOP
        while True:
            self.set_turn_order()
            for fighter in self.turn_order:
                if  fighter.is_dead():
                    continue
                self.clear_fighter_defense(fighter)
                self.cli.display_all_fighters(self.player_team, fighter, self.enemy_team)
                self.cli.display_fighters_turn(fighter.name, round)
                if fighter.is_player:
                    self.handle_player_turn(fighter)
                else:
                    self.cli.enemy_turn_pause()
                    self.handle_ai_turn(fighter)




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
