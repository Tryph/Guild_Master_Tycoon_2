from sources.Entity import Entity


class Hunter(Entity):

    def __init__(self, name):
        super().__init__(name, 'Hunter', 8)

