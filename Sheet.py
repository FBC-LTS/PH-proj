from random import choices, randint as rv

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
    
    def get_mod(self):
        return self.__mod

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
        ls = self.__std_atr
        chls = []
        for attribute in range(6):
            if len(ls) > 1:
                ch = choices(ls)[0]
                chls.append(ch)
                ls.remove(ch)
            else:
                chls.append(ls[0])

        self.__str = chls[0]
        self.__dex = chls[1]
        self.__con = chls[2]
        self.__int = chls[3]
        self.__wis = chls[4]
        self.__cha = chls[5]
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
        self.__race = 'HUMAN'
        self.__atts = atts
        self.__moves = {}
        self.__ch_class = 'Fighter'
        # Possible classes AND race match:
        self.__possMatch = {
            'HUMAN': ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Paladin', 'Ranger', 'Thief', 'Wizard'], 
            'ELF': ['Barbarian', 'Bard', 'Druid', 'Fighter', 'Ranger', 'Wizard'], 
            'DWARF': ['Barbarian', 'Cleric', 'Fighter'], 
            'HALFLING': ['Barbarian', 'Druid', 'Fighter', 'Thief']}
        self.__valid = True

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

    
    def class_setter(self, cclass):

        match = self.__possMatch[self.__race]
        if cclass.capitalize() in match:
            self.__ch_class = cclass.capitalize()
            self.__valid = True
        else:
            self.__valid = False
            self.__ch_class = cclass.capitalize()
            print(f'Invalid class value {cclass} \n Possible class to race {self.__race} : {match}')
    
    def race_setter(self, race): 
        if race.upper() in self.__possMatch.keys():
            match = self.__possMatch[race.upper()]
            if self.__ch_class in match:
                self.__race = race.upper()
                self.__valid = True
            else:
                self.__valid = False
                self.__race = race.upper()
                print(f'Invalid Class:{self.__ch_class.capitalize()} to race {self.__race.capitalize()}')
        else:
            print(f'Invalid race value {race.capitalize()}')
    
    def damage_update(): #$$$

        pass

    def show_self(self):
        sep = ('-=') * 15
        unsep = ('-' + ('_' * 21) + '-') 
        smpsep = ('-' * 23)
        print(
            f' {sep} \n--> Name: {self.__name} \n--> Race: {self.__race.capitalize()} \n--> class: {self.__ch_class}\n--> valida: {self.__valid}'
            f'\n   {unsep}\n   | Level: {self.__lvl}  |   XP: {self.__xp} |\n   {smpsep}\n'
            f'-   | att | val | mod|'
        )
        attrs = self.__atts.get_all_atts()
        attkeys = list(attrs.keys())
        mod = self.__atts.get_mod()
        for i in range(6):
            key = attkeys[i]
            print(f'-   | {key} : {attrs[key]:3} | {mod[key]:2} |')
        print(f'{sep}')