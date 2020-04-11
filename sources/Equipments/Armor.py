from sources.Equipments.Equipment import Equipment


class Armor(Equipment):
    def __init__(self, name, strength: int = 5):
        super().__init__(name, strength, 'Armor')
