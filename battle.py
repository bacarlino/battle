import random

class Battle:

    def __init__(self, player_team, enemy_team, cli):
        self.cli = cli
        self.player_team = player_team.full_list
        self.enemy_team = enemy_team.full_list
        self.turn_order = []


    def get_avail_targets(self, team: list):
        return [target for target in team if not target.is_dead()]

    def handle_player_turn(self, fighter):

        handler = {
            "attack": self.handle_attack,
            "defend": self.handle_defend,
            "skill": self.choose_skill,
            "item": self.choose_item,
            "invalid": self.handle_player_turn,
            "help": self.handle_help
        }

        while True:
            self.cli.display_options()
            choice = self.cli.get_main_option(fighter.name)
            choice = self.proc_choice(fighter, choice)
            if choice == "restart":
                return "restart"
            handler[choice](fighter)
            break


    def proc_choice(self, fighter, choice):

        if choice in ["a", "A", "attack", "Attack", "ATTACK"]:
            return "attack"
        elif choice in ["d", "D", "defend", "Defend", "DEFEND"]:
            return "defend"
        elif choice in ["s", "S", "skill", "Skill", "SKILL"]:
            return "skill"         
        elif choice in ["i", "I", "item", "Item", "ITEM"]:
            return "item"
        elif choice in ["r", "R", "restart", "Restart"]:
            return "restart"      
        elif choice in ["h", "H", "help", "Help"]:
            return "help"
        else:
            self.cli.display_invalid_command()
            return "invalid"

    def handle_attack(self, attacker, target=None):
        if attacker.is_player:
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("attack", avail_targets)
            if not target:
                self.cli.cancel_choice()
                self.handle_player_turn(attacker)
                return
        amt, is_crit = attacker.attack()
        if not amt:
            self.cli.display_miss(attacker.name)
            return
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
        if not skill:
                self.cli.cancel_choice()
                self.handle_player_turn(skill_user)
                return
        if skill_user.can_use_skill(skill):
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("skill_target", avail_targets, skill.name)
            if not target:
                self.cli.cancel_choice()
                self.handle_player_turn(skill_user)
                return
            self.handle_skill(skill_user, target, skill)
        else:    
            self.cli.display_skill_fail(skill_user.name, skill.sp)
            self.handle_player_turn(skill_user)

    def handle_skill(self, skill_user, target, skill):
        dmg = skill.rand_damage()

        if target.is_defending():
            dmg = int(dmg / 2)
        
        skill_user.use_skill(skill)
        target.take_damage(dmg)
        self.cli.display_use_skill(skill_user.name, skill, target.name, dmg)

        if skill.status:   
            target.add_status(skill.status)
            self.cli.display_add_status(target.name, skill.status.verb)
        
        if target.is_dead():
            self.cli.display_fighter_died(target.name)

    def choose_item(self, item_user):

        if not item_user.items:
            self.cli.display_no_items(item_user.name)
            self.handle_player_turn(item_user)

        item = self.cli.choose("item", item_user.items)

        if not item:
                self.cli.cancel_choice()
                self.handle_player_turn(item_user)
        
        elif item.type in ["heal", "buff"]:
            avail_targets = self.get_avail_targets(self.player_team)
            target = self.cli.choose("item_target", avail_targets, item.name)
            if not target:
                self.cli.cancel_choice()
                self.handle_player_turn(item_user)
            elif item.type == "heal":
                self.handle_buff_item(item_user, item, target)
            elif item.type == "buff":
                self.handle_buff_item(item_user, item, target)

        elif item.type in ["damage", "debuff"]:
            avail_targets = self.get_avail_targets(self.enemy_team)
            target = self.cli.choose("item_target", avail_targets, item.name)
            if not target:
                self.cli.cancel_choice()
                self.handle_player_turn(item_user)    
            elif item.type == "damage":
                self.handle_damage_item(item_user, item, target)
            elif item.type == "debuff":
                self.handle_damage_item(item_user, item, target)

    def handle_buff_item(self, item_user, item, item_target):
        self.cli.display_use_item(item_user.name, item.name, item_target.name)
        if item.amount > 0:
            item_target.add_hp(item.amount)
            self.cli.display_heal(item_target.name, item.amount)
        if item.status:   
            item_target.add_status(item.status)
            self.cli.display_add_status(item_target.name, item.status.verb)
        item_user.remove_item(item)

    def handle_damage_item(self, item_user, item, item_target):
        self.cli.display_use_item(item_user.name, item.name, item_target.name)
        if item.amount > 0:
            item_target.take_damage(item.amount)
            self.cli.display_take_damage(item_target.name, item.amount)
        if item.status:   
            item_target.add_status(item.status)
            self.cli.display_add_status(item_target.name, item.status.verb)
        item_user.remove_item(item)

    
    # def handle_damage_item(self, item_user, item, item_target):
    #     item_target.take_damage(item.amount)
    #     item_user.remove_item(item)
    #     self.cli.display_use_item(item_user.name, item.name, item_target.name)
    #     self.cli.display_take_damage(item_target.name, item.amount)
    #     if item_target.is_dead():
    #         self.cli.display_fighter_died(item_target.name)

    # def handle_buff_debuff_item(self, item_user, item, item_target):
    #     item_target.add_status(item.status)
    #     item_user.remove_item(item)
    #     self.cli.display_use_item(item_user.name, item.name, item_target.name)
    #     self.cli.display_add_status(item_target.name, item.status.name, item.status.description)

    # def handle_item(self, item_user, item, item_target):
    #     amount = item.amount
    #     item_user.use_item(item, item_target)
    #     self.cli.display_use_item(item_user.name, item, item_target.name, amount)
    #     if item_target.is_dead():
    #         self.cli.display_fighter_died(item_target.name)

    def handle_help(self,fighter):
        self.cli.display_help()
        self.handle_player_turn(fighter)

    def handle_ai_turn(self, fighter):
        avail_target = self.get_avail_targets(self.player_team)
        action = random.choice(fighter.actions)
        target = random.choice(avail_target)
        if fighter.skills:
            skill = random.choice(fighter.skills)
        if action == "attack":
            self.handle_attack(fighter, target)
        elif action == "defend":
            self.handle_defend(fighter)
        elif action == "skill":
            if fighter.has_skills():
                self.handle_skill(fighter, target, skill)
            else:
                self.handle_ai_turn(fighter)
        else:
            raise RuntimeError("A CPU action was not chosen or found")

    def set_turn_order(self):
        self.turn_order = self.player_team + self.enemy_team
        self.turn_order.sort(key=lambda player: player.speed, reverse=True)

    def pop_turn_order():
        pass

    def set_active_player(self):   
        self.active_player = self.turn_order[0]

    def char_turn_refresh(self, char):
        if char.defending:
            char.stop_defending()
        for status in char.status_lst():
            if status.name == "Bleeding":
                char.take_damage(status.amount)
                self.cli.display_take_damage(char.name, status.amount, status.verb)
            elif status.name == "Unconcious":
                self.cli.display_unconcious_effect(char.name)
                return False
            elif status.name == "Amped":
                self.turn_order.insert(0, char)
                self.cli.display_amped_effect(char.name)
        if char.is_dead():
            self.cli.display_fighter_died(char.name)
            return False
        char.update_statuses()
        return True
                
    def restart_game(self):
        pass

    def run(self):
        
        endgame = False
        round = 1

        self.cli.display_title()
        self.cli.display_instructions()
        self.cli.press_enter_pause()

        # MAIN BATTLE LOOP
        while True:
            self.set_turn_order()
            for fighter in self.turn_order:
                self.set_active_player()

                if fighter.is_dead():
                    continue                
                
                self.cli.display_fighters_turn(fighter.name, round)
                status_ok = self.char_turn_refresh(fighter)
                if not status_ok:
                    continue
                self.cli.display_all_fighters(self.player_team, fighter, self.enemy_team)
                
                if fighter.is_player:
                    restart = self.handle_player_turn(fighter)
                    if restart:
                        return restart

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
            
            # fighter.update_statuses()

            if endgame:
                self.cli.display_game_over()
                break    
            round += 1
