from __future__ import annotations


class Entity:
    name: str

    def __init__(self, name, class_, strength):
        self.name = name
        self.class_ = class_
        self.strength = strength

    def __sub__(self, other: Entity):
        """
        :return: True if the fighter_1 is stronger than the fighter 2, False
        otherwise.
        """
        return self.strength > other.strength

    def fight(self, other: Entity):
        return self - other
