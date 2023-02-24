# create a class for the enemies

damage_types = ['holy','ice','blood','darkness','steam','shadow']

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack(self, player):
        print(f'{self.name} attacks {player.name} for {self.attack} damage.')
        player.health -= self.attack

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} took {damage} damage.')

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f'{self.name} has {self.health} health.'




