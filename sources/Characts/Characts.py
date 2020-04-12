from __future__ import annotations

from typing import Optional, Union, Type, TypeVar


class Charact:
    value: int
    name: str
    short: str

    def __init__(self, name, short, value: Optional[int] = None):
        self.name = name
        self.short = short
        self.value = value if value else 0

    def __eq__(self, other: Union[Charact, int]) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value
        return self.value == other

    def __add__(self, other) -> int:
        if isinstance(other, type(self)):
            return self.value + other.value
        return self.value + other

    def __str__(self) -> str:
        result = f'{self.short}: {self.value}'
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self, *args, **kwargs) -> int:
        """
        :return: return data with primitive type.
        """
        return self.value

    def __bool__(self):
        return bool(self.value)


class Strength(Charact):
    def __init__(self, value: Optional[int] = None):
        super().__init__('Strength', 'str', value)


class Intelligence(Charact):
    def __init__(self, value: Optional[int] = None):
        super().__init__('Intelligence', 'int', value)


class Dexterity(Charact):
    def __init__(self, value: Optional[int] = None):
        super().__init__('Dexterity', 'dex', value)


class HitPoint(Charact):
    def __init__(self, value: Optional[int] = None):
        super().__init__('Hit Point', 'HP', value)


class Wounds(Charact):
    def __init__(self, value: Optional[int] = None):
        super().__init__('Wounds', 'W', value)


Stat_ = TypeVar('Stat_', bound=Charact)


def _set_stat(value: Union[Charact, int, None], type_: Type[Stat_]) -> Stat_:
    """
    :param value: the value of the Stat instance we want to create.
    :param type_: the subclass of Stat we want to instantiate.
    :return: an instance of the subclass passed in type_.
    """
    if isinstance(value, int):
        return type_(value)
    elif isinstance(value, type_):
        return value
    elif value is None:
        return type_()


class Characts:
    strength: Strength
    intelligence: Intelligence
    dexterity: Dexterity
    hit_point: HitPoint
    wounds: Wounds

    def __init__(
            self,
            strength: Optional[Strength, int] = None,
            intelligence: Optional[Intelligence, int] = None,
            dexterity: Optional[Dexterity, int] = None,
            hit_point: Optional[HitPoint, int] = None,
            wounds: Optional[Wounds, int] = None,
    ):
        self.strength = _set_stat(strength, Strength)
        self.intelligence = _set_stat(intelligence, Intelligence)
        self.dexterity = _set_stat(dexterity, Dexterity)
        self.hit_point = _set_stat(hit_point, HitPoint)
        self.wounds = _set_stat(wounds, Wounds)

    def __str__(self):
        characts = list()
        if self.strength:
            characts.append(self.strength)
        if self.intelligence:
            characts.append(self.intelligence)
        if self.dexterity:
            characts.append(self.dexterity)
        if self.hit_point:
            characts.append(self.hit_point)
        if self.wounds:
            characts.append(self.wounds)
        result = f'characts: {tuple(characts)}'
        return result

    def __call__(self, *args, **kwargs):
        """
        :return: return data with primitive type.
        """
        return (self.strength(), self.intelligence(), self.dexterity(),
                self.hit_point)
