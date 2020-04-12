from typing import Optional

from sources.Characts.Characts import Characts


class Equipment:
    name: str
    characts: Characts
    type_: str

    def __init__(self, name: str, type_: str,
                 characteristics: Optional[Characts] = None):
        self.name = name
        self.type_ = type_
        self.characts = characteristics if characteristics else Characts()

    def __str__(self):
        result = f'{self.type_} "{self.name}"'
        return result

    def __repr__(self):
        return self.__str__()


class Weapon(Equipment):
    def __init__(self, name, characteristics: Optional[Characts] = None):
        super().__init__(name, 'Weapon', characteristics)


class Armor(Equipment):
    def __init__(self, name, characteristics: Optional[Characts] = None):
        super().__init__(name, 'Armor', characteristics)


class Equipments:
    weapon: Weapon
    armor: Armor

    def __init__(self, weapon: Optional[Weapon] = None,
                 armor: Optional[Armor] = None):
        self.weapon = weapon if weapon else None
        self.armor = armor if armor else None

    def __str__(self):
        equips = list()
        if self.weapon:
            equips.append(self.weapon)
        if self.armor:
            equips.append(self.armor)
        result = f'Equipments: {tuple(equips)}'
        return result

    @property
    def strength(self):
        return self.weapon.characts.strength + self.armor.characts.strength

    @property
    def intelligence(self):
        return self.weapon.characts.intelligence + self.armor.characts.intelligence

    @property
    def dexterity(self):
        return self.weapon.characts.dexterity + self.armor.characts.dexterity

    @property
    def hit_point(self):
        return self.weapon.characts.hit_point + self.armor.characts.hit_point

    @property
    def wounds(self):
        return self.weapon.characts.wounds + self.armor.characts.wounds
