from sources.Equipments.Equipment import Equipment


class Weapon(Equipment):
    def __init__(self, name, strength: int = 1):
        super().__init__(name, strength, 'Weapon')
