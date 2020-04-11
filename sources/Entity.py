from __future__ import annotations

from typing import Optional, List

from sources.Equipments.Equipments import Equipments


class Entity:
    name: str
    class_: str
    strength: int
    equipments: Equipments

    def __init__(self, name, class_, strength,
                 equipments: Optional[Equipments] = None):
        self.name = name
        self.class_ = class_
        self._strength = strength
        self.equipments = equipments

    def __sub__(self, other: Entity):
        """
        :return: True if the fighter_1 is stronger than the fighter 2, False
        otherwise.
        """
        return self.strength > other.strength

    def fight(self, other: Entity):
        return self - other

    @property
    def strength(self):
        return self._strength + self.equipments.strength
