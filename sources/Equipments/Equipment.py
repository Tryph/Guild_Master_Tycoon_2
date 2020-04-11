class Equipment:
    name: str
    strength: int
    type_: str

    def __init__(self, name: str, strength: int, type_: str):
        self.name = name
        self.strength = strength
        self.type_ = type_