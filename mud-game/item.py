
rarity = {
    'common': 1,
    'uncommon': 2,
    'rare': 3,
    'epic': 4,
    'legendary': 5,
    'mythic': 6,
    'unique': 7,
    'artifact': 8,
    'godly': 9
}

type = {
    'healing': 1,
    'damage': 2,
    'weapon': 3,
    'armor': 4
}

class Item:
    def __init__(self, name, description, type, value, quantity):
        self.name = name
        self.description = description
        self.type = type
        self.value = value
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def use_item(self, player):
        if self.type == 'healing':
            player.health += self.value
            print(f'You used {self.name} and healed for {self.value} health.')
            self.quantity -= 1
        elif self.type == 'damage':
            player.health -= self.value
            print(f'You used {self.name} and took {self.value} damage.')
            self.quantity -= 1
        elif self.type == 'weapon':
            player.attack += self.value
            print(f'You used {self.name} and increased your attack by {self.value}.')
            self.quantity -= 1
        elif self.type == 'armor':
            player.defense += self.value
            print(f'You used {self.name} and increased your defense by {self.value}.')
            self.quantity -= 1
        else:
            print(f'You cannot use {self.name}.')


