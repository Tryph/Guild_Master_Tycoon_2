from sources.Entity import Entity


class Mage(Entity):

    def __init__(self, name):
        super().__init__(name, 'Mage', 5)
