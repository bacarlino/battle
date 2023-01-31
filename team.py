

class Team:
    def __init__(self, char_list):
        self.full_list = char_list
        self.active_list = char_list.copy()
    
    def __str__(self):
        return str(self.full_list)

    def get_full_list(self):
        return self.full_list

    def get_active_list(self):
        return self.active_list

    def add_char(self, char):
        self.full_list.append(char)
        self.active_list.append(char)
    
    def remove_char(self, char):
        self.full_team.remove(char)
    
    def set_char_active(self, char):
        if char not in self.active_list:
            self.active_list.append(char)
        else:
            print("Char already in self.active_list")

    def set_char_inactive(self, char):
        if char in self.active_list:
            self.active_list.remove(char)
        else:
            print("Char not in self.active_list")

    def set_all_active(self, char):
        self.active_list = self.full_list.copy()

if __name__ == "__main__":
    test_team = build_team(2)
    print(test_team)
    print(test_team.active_list)
    print(test_team.get_active_list())
    print(test_team.set_char_inactive(test_team.active_list[0]))
    print(test_team.get_full_list())
    print(test_team.get_active_list())
    print(test_team.full_list[1] is test_team.active_list[0])
