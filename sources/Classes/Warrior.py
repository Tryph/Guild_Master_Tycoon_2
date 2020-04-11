from typing import Optional

from sources.Entity import Entity
from sources.Equipments.Armor import Armor
from sources.Equipments.Equipments import Equipments
from sources.Equipments.Weapon import Weapon


class Warrior(Entity):

    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(Weapon('Sword', 10),
                                    Armor('Full plate armor', 7))
        super().__init__(name, 'Warrior', 10, equipments)

