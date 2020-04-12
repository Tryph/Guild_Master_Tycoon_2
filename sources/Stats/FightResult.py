class FightResult:
    win: bool
    time: int

    def __init__(self, win: bool, time: int, overkill: int):
        self.win = win
        self.overkill = overkill
        self.time = time
