class Entity:

  def __init__(self, emoji, health, damage) -> None:
    self.emoji = emoji
    self.health = health
    self.max_health = health
    self.damage = damage
    self.inventory = []

  def print_health(self):
    print(f'{self.emoji}: {self.health} ❤')

  def attack(self, enemy):
    enemy.health -= self.damage
    enemy.health = max(0, enemy.health)

  def add_item(self, item: dict):
    self.inventory.append(item)

  def print_inventory(self):
    for i in self.inventory:
      print('-', i['name'], ': ', i['description'])
