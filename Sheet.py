
from typing_extensions import Self

class Personagem:
    def __init__(self, name, level, race, stats, armor, damage, moves) -> None:
        self.__nome = name
        self.__lv = level
        self.__raca = race
        self.__stats = stats
        self.__armor = armor
        self.__damage = damage
        self.__moves = moves
    

class PLevel:
    def __init__(Self, lvl, xp=0 ) -> None:
        Self.__lvl = lvl
        Self.__xp = xp


class PStats(Self):
    def __init__(Self, stats) -> None:
        Self.__stats = stats


class PMoves(Self):
    def __init__(self, name, desc) -> None:
        self.__name = name
        self.__desc = desc