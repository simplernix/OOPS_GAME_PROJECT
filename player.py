from character import Character
import random

class Player(Character):
    """Player character class with inventory and progression."""
    
    def __init__(self, name: str, char_class: str = "Warrior"):
        """Initialize a player character.        
        Args:
            name (str): Player name
            char_class (str): Character class type
        """
        super().__init__(name, health=100, attack=15, defense=5)
        self._char_class = char_class
        self._inventory = []
        self._experience = 0
        self._gold = 0
    
    @property
    def char_class(self) -> str:
        """Get character class (Encapsulation)."""
        return self._char_class
    
    @property
    def inventory(self) -> list:
        """Get inventory items."""
        return self._inventory
    
    @property
    def gold(self) -> int:
        """Get gold amount."""
        return self._gold
    
    def add_item(self, item) -> None:
        """Add item to inventory (Composition)."""
        self._inventory.append(item)
    
    def remove_item(self, item) -> None:
        """Remove item from inventory."""
        if item in self._inventory:
            self._inventory.remove(item)
    
    def add_gold(self, amount: int) -> None:
        """Add gold to inventory."""
        self._gold += amount
    
    def attack_action(self) -> int:
        """Polymorphic attack - overridden by subclasses."""
        return super().attack_action()
    
    def special_ability(self) -> str:
        """Special ability placeholder."""
        return "No special ability"


class Warrior(Player):
    """Warrior class with high defense and melee attacks (Inheritance & Polymorphism)."""    
    
    def __init__(self, name: str):
        super().__init__(name, "Warrior")
        self._health = 150
        self._max_health = 150
        self._attack = 18
        self._defense = 10
    
    def attack_action(self) -> int:
        """Warrior performs a physical strike (Polymorphism)."""
        variance = random.randint(-1, 4)
        critical_hit = random.random() < 0.15
        damage = self._attack + variance
        if critical_hit:
            damage *= 1.5
        return int(max(1, damage))
    
    def special_ability(self) -> str:
        """Warrior's special ability: Shield Bash."""
        self._defense += 3
        return "Shield Bash activated! Defense +3"


class Mage(Player):
    """Mage class with high attack but low defense (Inheritance & Polymorphism)."""    
    
    def __init__(self, name: str):
        super().__init__(name, "Mage")
        self._health = 80
        self._max_health = 80
        self._attack = 25
        self._defense = 3
        self._mana = 50
        self._max_mana = 50
    
    @property
    def mana(self) -> int:
        """Get current mana."""
        return self._mana
    
    def attack_action(self) -> int:
        """Mage performs a magical attack (Polymorphism)."""
        if self._mana >= 10:
            self._mana -= 10
            variance = random.randint(0, 5)
            return max(1, self._attack + variance)
        return random.randint(3, 8)  # Weak attack without mana    
    
    def special_ability(self) -> str:
        """Mage's special ability: Fireball."""
        if self._mana >= 30:
            self._mana -= 30
            return "Fireball cast! Massive damage incoming!"
        return "Not enough mana for Fireball!"
    
    def restore_mana(self, amount: int) -> None:
        """Restore mana points."""
        self._mana = min(self._max_mana, self._mana + amount)


class Archer(Player):
    """Archer class with balanced stats and ranged attacks (Inheritance & Polymorphism)."""    
    
    def __init__(self, name: str):
        super().__init__(name, "Archer")
        self._health = 110
        self._max_health = 110
        self._attack = 20
        self._defense = 6
        self._arrows = 30
    
    @property
    def arrows(self) -> int:
        """Get arrow count."""
        return self._arrows
    
    def attack_action(self) -> int:
        """Archer performs a ranged attack (Polymorphism)."""
        if self._arrows > 0:
            self._arrows -= 1
            critical_chance = random.random()
            if critical_chance < 0.25:  # 25% critical hit chance
                return int(self._attack * 1.75)
            variance = random.randint(-2, 2)
            return max(1, self._attack + variance)
        return random.randint(2, 5)  # Weak punch without arrows    
    
    def special_ability(self) -> str:
        """Archer's special ability: Rain of Arrows."""
        if self._arrows >= 5:
            self._arrows -= 5
            return "Rain of Arrows cast! Multiple hits incoming!"
        return "Not enough arrows for Rain of Arrows!"
    
    def replenish_arrows(self, amount: int) -> None:
        """Add arrows to inventory."""
        self._arrows = min(100, self._arrows + amount)