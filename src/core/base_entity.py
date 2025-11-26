from abc import ABC, abstractmethod

class BaseEntity(ABC):
    """Abstract base class for all game entities."""
    
    def __init__(self, name: str, health: int, attack: int):
        """
        Initialize a game entity.
        
        Args:
            name (str): Entity name
            health (int): Health points
            attack (int): Attack power
        """
        self._name = name
        self._health = health
        self._attack = attack
        self._max_health = health
    
    @property
    def name(self) -> str:
        """Get entity name."""
        return self._name
    
    @property
    def health(self) -> int:
        """Get current health (Encapsulation)."""
        return self._health
    
    @property
    def attack(self) -> int:
        """Get attack power."""
        return self._attack
    
    @abstractmethod
    def is_alive(self) -> bool:
        """Check if entity is alive (Abstract method)."""
        pass
    
    @abstractmethod
    def take_damage(self, amount: int) -> None:
        """Apply damage to entity (Abstract method - Polymorphism)."""
        pass
    
    @abstractmethod
    def attack_action(self) -> int:
        """Perform an attack (Polymorphism)."""
        pass
