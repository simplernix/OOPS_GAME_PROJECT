class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health=150, attack=15)

    def battle_cry(self):
        return 'For honor!'


class Mage(Player):
    def __init__(self, name):
        super().__init__(name, health=100, attack=25)

    def cast_spell(self):
        return 'Casting a powerful spell!'


class Archer(Player):
    def __init__(self, name):
        super().__init__(name, health=120, attack=20)

    def shoot_arrow(self):
        return 'Shooting an arrow!'
