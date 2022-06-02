from random import randint  as rv
from secrets import choice

def between(val, mini, maxi):
    # Value is between mini and maxi?
    if val >= mini and val <= maxi:
        return True
    else:
        return False


#class CharAttributes, here will be added value for each attribute and calculated all modifiers
class CharAttributes:
    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0) -> None:
        self.__std_atr = [8, 9, 12, 13, 15, 16]
        self.__str = strength
        self.__dex = dexterity
        self.__con = constitution
        self.__int = intelligence
        self.__wis = wisdom
        self.__cha = charisma
        self.__mod ={
            'str': 0, 
            'dex': 0, 
            'con': 0, 
            'int': 0, 
            'wis': 0, 
            'cha': 0
        }
        self.__auto_upmods()

    def get_all_atts(self):
        atts = {
            'str': self.__str, 
            'dex': self.__dex, 
            'con': self.__con, 
            'int': self.__int, 
            'wis': self.__wis, 
            'cha': self.__cha
        }
        return atts
    
    def __auto_upmods(self):
        # Calculates all modifiers
        sts_list = [self.__str, self.__dex, self.__con, self.__int, self.__wis, self.__cha]
        mod_list = []
        for i in sts_list:
            if between(i, 1, 3):
                mod_list.append(-3)
            elif between(i, 4, 5):
                mod_list.append(-2)
            elif between(i, 6, 8):
                mod_list.append(-1)
            elif between(i, 9, 12):
                mod_list.append(0)
            elif between(i, 13, 15):
                mod_list.append(1)
            elif between(i, 16, 17):
                mod_list.append(2)
            elif i >= 18:
                mod_list.append(3)
            else:
                mod_list.append(-100)

        self.__mod.update({        
            'str': mod_list[0], 
            'dex': mod_list[1], 
            'con': mod_list[2], 
            'int': mod_list[3], 
            'wis': mod_list[4], 
            'cha': mod_list[5]}
            )
    
    def choice_randon_setter(self):
        # All attributes will receive the values [8, 9, 12, 13, 15, 16] randomly
        self.__str = choice(self.__std_atr)
        self.__dex = choice(self.__std_atr)
        self.__con = choice(self.__std_atr)
        self.__int = choice(self.__std_atr)
        self.__wis = choice(self.__std_atr)
        self.__cha = choice(self.__std_atr)
        self.__auto_upmods()
    
    def full_randon_setter(self, min=0, max=18): 
        # All attributes will receive random values
        self.__str = rv(min, max)
        self.__dex = rv(min, max)
        self.__con = rv(min, max)
        self.__int = rv(min, max)
        self.__wis = rv(min, max)
        self.__cha = rv(min, max)
        self.__auto_upmods()
    


class Character:
    def __init__(self, atts):
        self.__lvl = 0
        self.__xp = 0
        self.__armor = 0
        self.__name = 'name'
        self.__race = 'race'
        self.__atts = atts
        self.__moves = {}
        self.__ch_class = 'class'
        # Possible classes according to race:
        self.__posclass = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Paladin', 'Ranger', 'Thief', 'Wizard'] 
        # Possible reces according to class:
        self.__posrace = ['HUMAN', 'ELF', 'DWARF', 'HALFLING'] 

    def get_lvl(self):
        return self.__lvl

    def get_xp(self):
        return self.__xp
    
    def get_moves(self):
        return self.__moves

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race
    
    def get_atts(self):
        return self.__atts
    
    def get_armor(self):
        return self.__armor
    
    def race_setter(self, race):
        self.__race = race

    def name_setter(self, name):
        self.__name = name

    def armor_setter(self, armor):
        self.__armor = armor

    def xp_setter(self, xp):
        self.__xp += xp
        to_lvlup = self.__lvl + 8
        if self.__xp >= to_lvlup:
            self.__xp -= to_lvlup
            self.__lvl += 1
    
    def newmove_setter(self, move_name, move_desc):
        self.__moves[move_name] = move_desc
    
    def class_setter(self, cclass): #$$
        if cclass.upper() in self.__posclass:
            self.__ch_class = cclass
    
    def race_setter(self, race): #$$
        if race.upper() in self.__posrace:
            self.__race = race
