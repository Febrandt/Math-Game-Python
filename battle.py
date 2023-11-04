from os import system
from random import randrange

from entity import Entity
from items import item


class Battle:

  def __init__(self, enemy, player) -> None:
    self.enemy = enemy
    self.player = player

  def print_healths(self):
    self.player.print_health()
    self.enemy.print_health()

  def guess_number(self):
    from game import singleton_guess
    guess = randrange(1, singleton_guess+1)
    print('Você está ganhando demais!!!')
    answer = input(f'Adivinhe um número de 1-{singleton_guess}: ')

    return int(answer) == guess

  def guess_calculation(self):
    n1 = randrange(1, 10)
    n2 = randrange(1, 10)
    n3 = randrange(1, 4)
    total = n1 * n2 * n3

    answer = input(f'Quanto é {n1} * {n2} * {n3}? ')
    return int(answer) == total

  def result(self):
    from game import singleton_wins
    self.print_healths()
    wins = 0

    while self.player.health > 0 and self.enemy.health > 0:

      if wins == singleton_wins:
        if self.guess_number():
          print('Correto!')
          self.player.attack(self.enemy)
          self.print_healths()
        else:
          print('Errado!!!')
          self.enemy.attack(self.player)
          self.print_healths()
        wins = 0

      if self.player.health <= 0 or self.enemy.health <= 0:
        break

      if self.guess_calculation():
        self.player.attack(self.enemy)
        wins += 1
        self.print_healths()
      else:
        self.enemy.attack(self.player)
        self.print_healths()

    self.player.health = self.player.max_health

    if self.player.health <= 0:
      system('cls||clear')
      self.print_healths()
      print('Você Perdeu!')
      return False

    if self.enemy.health <= 0:
      system('cls||clear')
      self.print_healths()
      print(f'Você ganhou do {self.enemy.emoji}!')
      self.player.inventory.extend(self.enemy.inventory)
      print('Você ganhou os seguintes items: ')
      self.enemy.print_inventory()
      if self.enemy.inventory == []:
        print('Nada')
      return True
