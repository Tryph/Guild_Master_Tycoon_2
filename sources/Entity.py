from __future__ import annotations

from asyncio import get_event_loop, FIRST_COMPLETED, wait, sleep
from typing import Optional

from sources.Characts.Characts import Characts, Strength, Wounds
from sources.Equipments.Equipments import Equipments, Weapon, Armor
from sources.time_constants import ATTACK_BASE


class Entity:
    name: str
    class_: str
    _statistics: Characts
    _equipments: Equipments

    def __init__(self, name, class_, statistics: Optional[Characts] = None,
                 equipments: Optional[Equipments] = None):
        self.name = name
        self.class_ = class_
        self._statistics = statistics if statistics else Characts()
        self._equipments = equipments if equipments else Equipments()

    def __sub__(self, other: Entity):
        """
        :return: True if the fighter_1 is stronger than the fighter 2, False
        otherwise.
        """
        loop = get_event_loop()
        task_1 = self.fight(other)
        task_2 = other.fight(self)
        tasks = [task_1, task_2]

        finished, unfinished = loop.run_until_complete(
            wait(tasks, return_when=FIRST_COMPLETED))
        for task in unfinished:
            task.cancel()
        return self.is_alive

    def __str__(self):
        return f'{self.class_} "{self.name}"'

    def __repr__(self):
        return self.__str__()

    @property
    def strength(self) -> int:
        return self._statistics.strength + self.equipments.strength

    @property
    def intelligence(self) -> int:
        return self._statistics.intelligence + self.equipments.intelligence

    @property
    def dexterity(self) -> int:
        return self._statistics.dexterity + self.equipments.dexterity

    @property
    def hit_point(self) -> int:
        return self._statistics.hit_point + self.equipments.hit_point

    @property
    def wounds(self) -> int:
        return self._statistics.wounds + self.equipments.wounds

    @property
    def attack_speed(self) -> float:
        return self._statistics.attack_speed + self.equipments.attack_speed

    @property
    def HP_to_death(self) -> int:
        return self.hit_point - self.wounds

    @property
    def equipments(self) -> Equipments:
        return self._equipments

    @property
    def is_alive(self) -> bool:
        return self.hit_point > self.wounds

    def harm(self, damages: int) -> None:
        self._statistics.wounds = Wounds(self._statistics.wounds + damages)

    def hit(self, other: Entity):
        other.harm(self.strength)
        return other.HP_to_death

    async def fight(self, other: Entity):
        while other.is_alive and self.is_alive:
            await sleep(ATTACK_BASE/self.attack_speed)
            self.hit(other)
        return


class Mage(Entity):
    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(
                Weapon('Staff', Characts(strength=Strength(-1))),
                Armor('Wizard dress', Characts(strength=Strength(-1))))
        stats = Characts(3, 10, 5, 10, 0, 1.5)
        super().__init__(name, 'Mage', stats, equipments)


class Hunter(Entity):
    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(
                Weapon('Bow', Characts(strength=Strength(3))),
                Armor('Leather armor', Characts(strength=Strength(5))))
        stats = Characts(3, 5, 10, 10, 0, 0.9)
        super().__init__(name, 'Hunter', stats, equipments)


class Warrior(Entity):
    def __init__(self, name, equipments: Optional[Equipments] = None):
        if not equipments:
            equipments = Equipments(
                Weapon('Sword', Characts(strength=Strength(10))),
                Armor('Full plate armor', Characts(strength=Strength(7))))
        stats = Characts(10, 3, 5, 10, 0, 1.)
        super().__init__(name, 'Warrior', stats, equipments)
