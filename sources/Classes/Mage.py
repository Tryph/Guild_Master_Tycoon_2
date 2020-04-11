from typing import Optional

from sources.Entity import Entity
from sources.Equipments.Armor import Armor
from sources.Equipments.Equipments import Equipments
from sources.Equipments.Weapon import Weapon


class Mage(Entity):

    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(Weapon('Staff', -1),
                                    Armor('Wizard dress', -1))
        super().__init__(name, 'Mage', 5, equipments)
