from player import Player
from enemy import Enemy
from combat import Combat

def main():
    player = Player("Hero", 100, 10)
    enemy = Enemy("Goblin", 50, 5)
    combat = Combat(player, enemy)
    combat.start()

if __name__ == "__main__":
    main()