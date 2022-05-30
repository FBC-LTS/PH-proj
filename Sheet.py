
class Character:
    def __init__(self, name='', race={}, stats={}, armor=0, damage=0):
        self.__name = name
        self.__race = race
        self.__stats = stats
        self.__armor = armor
        self.__damage = damage
    
    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race
    
    def get_stats(self):
        return self.__stats
    
    def get_armor(self):
        return self.__armor
    
    def get_damage(self):
        return self.__damage
    
    def armor_setter(self, armor):
        self.__armor = armor
    
    def damage_setter(self, damage):
        self.__damage = damage
        
    def stats_setter(self, atr, value):
        self.__stats[atr] = value
    

class CPlayer(Character):
    def __init__(self, name='', race={}, stats={}, armor=0, damage=0, lvl=1, xp=0, moves={}):
        super().__init__(name, race, stats, armor, damage)
        self.__lvl = lvl
        self.__xp = xp
        self.__moves = moves

    def get_lvl(self):
        return self.__lvl

    def get_xp(self):
        return self.__xp
    
    def get_moves(self):
        return self.__moves

    def get_armor(self):
        return super().get_armor()
    
    def get_damage(self):
        return super().get_damage()
    
    def get_name(self):
        return super().get_name()
    
    def get_race(self):
        return super().get_race()
    
    def get_stats(self):
        return super().get_stats()

    def xp_setter(self, xp):
        self.__xp += xp
        to_lvlup = self.__lvl + 8
        if self.__xp >= to_lvlup:
            self.__xp -= to_lvlup
            self.__lvl += 1
    
    def newmove_setter(self, move):
        self.__moves.add(move)




class MultipleSheetCreator:
    def __init__(self):
        self.__sheet_list = []
    
    def create_sheet(self, name, race, stats, armor, damage, player= False):
        char = Character(name, race, stats, armor, damage)
        if player:
            player_sheet = CPlayer(name, race, stats, armor, damage, 1, 0, {})
            self.__sheet_list.append(player_sheet)
            return player_sheet
        self.__sheet_list.append(char)
        return char

    def get_sheet_list(self):
        return self.__sheet_list