from sources.Equipments.Armor import Armor
from sources.Equipments.Weapon import Weapon


class Equipments:
    weapon: Weapon
    armor: Armor

    def __init__(self, weapon: Weapon, armor: Armor):
        self.weapon = weapon
        self.armor = armor

    @property
    def strength(self):
        return self.weapon.strength + self.armor.strength
