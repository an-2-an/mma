class Fighter:
    def __init__(self, name, arsenal):
        self.name = name
        self.arsenal = arsenal
        self.health = 100

    def got_damage(self, damage):
        self.health = self.health - damage if self.health > damage else 0