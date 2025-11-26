from src.core.base_entity import BaseEntity
import random

class Character(BaseEntity):
    """Base character class implementing core game mechanics."""
    
    def __init__(self, name: str, health: int, attack: int, defense: int = 5):
        """
        Initialize a character.
        
        Args:
            name (str): Character name
            health (int): Health points
            attack (int): Attack power
            defense (int): Defense rating
        """
        super().__init__(name, health, attack)
        self._defense = defense
        self._level = 1
        self._experience = 0
    
    @property
    def defense(self) -> int:
        """Get defense rating (Encapsulation)."""
        return self._defense
    
    @property
    def level(self) -> int:
        """Get character level."""
        return self._level
    
    def is_alive(self) -> bool:
        """Check if character is alive (Override from BaseEntity)."""
        return self._health > 0
    
    def take_damage(self, amount: int) -> None:
        """Apply damage reducing defense (Polymorphism)."""
        reduced_damage = max(1, amount - self._defense // 2)
        self._health -= reduced_damage
        if self._health < 0:
            self._health = 0
    
    def attack_action(self) -> int:
        """Perform basic attack with random variance (Polymorphism)."""
        variance = random.randint(-2, 3)
        return max(1, self._attack + variance)
    
    def level_up(self) -> None:
        """Increase character level and stats."""
        self._level += 1
        self._health = self._max_health + (self._level * 10)
        self._attack += 2
        self._defense += 1
    
    def heal(self, amount: int) -> None:
        """Restore health (Encapsulation)."""
        self._health = min(self._max_health, self._health + amount)
    
    def gain_experience(self, amount: int) -> None:
        """Gain experience and potentially level up."""
        self._experience += amount
        if self._experience >= 100:
            self.level_up()
            self._experience = 0
