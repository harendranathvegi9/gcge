class Phase:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Phase {0}".format(self.name)

    def __eq__(self, other):
        return self.name == other

class Turn:
    def __init__(self, player):
        self.player = player
    def __str__(self):
        return "Player {0}".format(self.player)

class Round:
    def __init__(self):
        pass
