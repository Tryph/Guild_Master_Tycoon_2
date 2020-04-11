from sources.Entity import Entity


class Warrior(Entity):

    def __init__(self, name):
        super().__init__(name, 'Warrior', 10)

