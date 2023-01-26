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

        handler = {
            "attack": self.handle_attack,
            "defend": self.handle_defend,
            "skill": self.choose_skill,
            "item": self.choose_item
        }

        while True:
            self.cli.display_options()
            choice = self.cli.get_main_option(fighter.name)
            choice = self.proc_choice(fighter, choice)
            handler[choice](fighter)
            break


    def proc_choice(self, fighter, choice):

        if choice in ["a", "A", "attack", "Attack", "ATTACK", "1"]:
            return "attack"

        elif choice in ["d", "D", "defend", "Defend", "DEFEND", "2"]:
            return "defend"

        elif choice in ["s", "S", "skill", "Skill", "SKILL",  "3"]:
            return "skill"
            
        elif choice in ["i", "I", "item", "Item", "ITEM", "4"]:
            return "item"

        elif choice in ["r", "R", "run", "Run", "RUN", "5"]:
            print("RUNNING AWAY!")

        else:
            self.cli.display_invalid_command()
            self.cli.display_options()

    def handle_attack(self, attacker, target=None):
        if attacker.is_player:
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("attack", avail_targets)
        amt, is_crit = attacker.attack()
        if target.defending:
            amt = int(amt / 2)
        target.take_damage(amt)
        self.cli.display_attack(attacker, target, amt, is_crit)
        if target.is_dead():
            self.cli.display_fighter_died(target.name)

    def handle_defend(self, defender):
        defender.defend()
        self.cli.display_defend(defender)

    def choose_skill(self, skill_user):
  
        skill = self.cli.choose("skill", skill_user.skills)
        if skill_user.can_use_skill(skill):
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("skill_target", avail_targets, skill.name)
            self.handle_skill(skill_user, target, skill)
        else:    
            self.cli.display_skill_fail(skill_user.name, skill.sp)
            self.cli.display_options()

    def handle_skill(self, skill_user, target, skill):

        # damage calc method?
        dmg = skill.dmg
        adj = dmg*0.25
        dmg = int(random.uniform(dmg - adj, dmg + adj))
        if target.defending:
            dmg = int(dmg / 2)
        
        skill_user.use_skill(skill)
        target.take_damage(dmg)
        self.cli.display_use_skill(skill_user.name, skill, target.name, dmg)
        if target.is_dead():
            self.cli.display_fighter_died(target.name)

    def choose_item(self, item_user):
        if not item_user.items:
            self.cli.display_no_items(item_user.name)
            self.handle_player_turn(item_user)
            return
        item = self.cli.choose("item", item_user.items)
        if item.type == "heal":
            avail_targets = self.get_avail_targets(self.player_team)
            target = self.cli.choose("item_target", avail_targets, item.name)
            self.handle_heal_hp_item(item_user, item, target)
        elif item.type == "damage":
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("item_target", avail_targets, item.name)
            self.handle_damage_item(item_user, item, target)
        elif item.type == "buff":
            pass
        elif item.type == "debuff":
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("item_target", avail_targets, item.name)
            self.handle_debuff_item(item_user, item, target)

    def handle_heal_hp_item(self, item_user, item, item_target):
        item_user.remove_item(item)
        item_target.add_hp(item.amount)
        self.cli.display_use_item(item_user.name, item.name, item_target.name)
        self.cli.display_heal(item_target.name, item.amount)
    
    def handle_damage_item(self, item_user, item, item_target):
        item_user.remove_item(item)
        item_target.take_damage(item.amount)
        self.cli.display_use_item(item_user.name, item.name, item_target.name)
        self.cli.display_take_damage(item_target.name, item.amount)
        if item_target.is_dead():
            self.cli.display_fighter_died(item_target.name)

    def handle_debuff_item(self, item_user, item, item_target):
        item_user.remove_item(item)
        item_target.add_status(item.status)
        self.cli.display_use_item(item_user.name, item.name, item_target.name)
        self.cli.display_add_status(item_target.name, item.status)


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
        if action == "attack":
            self.handle_attack(fighter, target)
        elif action == "defend":
            self.handle_defend(fighter)
        elif action == "skill":
            if fighter.can_use_skill(skill):
                self.handle_skill(fighter, target, skill)
            else:
                self.handle_ai_turn(fighter)
        else:
            raise RuntimeError("A CPU action was not chosen or found")

    def set_turn_order(self):
        self.turn_order = self.player_team + self.enemy_team
        self.turn_order.sort(key=lambda player: player.speed)
    
    
    def clear_fighter_defense(self, fighter):
        if fighter.defending:
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
                self.clear_fighter_defense(fighter)
                if  fighter.is_dead():
                    continue                
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
