from typing import Optional

from sources.Entity import Entity
from sources.Equipments.Armor import Armor
from sources.Equipments.Equipments import Equipments
from sources.Equipments.Weapon import Weapon


class Hunter(Entity):

    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(Weapon('Bow', 3),
                                    Armor('Leather armor', 5))
        super().__init__(name, 'Hunter', 8, equipments)

