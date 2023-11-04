from item import item

from time import sleep
from battle import Battle
from entity import Entity
from items import mage_chest_key_item
from scenes.scene import Scene


class ElfKingScene(Scene):

  def __init__(self):
    super().__init__(name='Castelo do Rei',
                     description='O Rei te propõe uma batalha! Para testar sua habilidade!',
                     choices={
                         'Batalhar': self.battle,
                         'Roubar a Esposa': self.wife
                     })

  def battle(self):
    from scenes.start_scene2 import StartScene2

    from game import singleton_game
    king = Entity('👑🧝‍♂️',400,25)
    battle = Battle(king,singleton_game.player)
    if battle.result():
      print('Você conseguiu derrotar o Rei!')
      sleep(0.5)
      print('Ele então decide lhe nominar o Rei dos Elfos!')
      sleep(0.5)
      print('Você sai correndo, pois ninguém merece tal responsabilidade!')
      singleton_game.change_scene_to(StartScene2())


  def wife(self):
    from scenes.start_scene2 import StartScene2

    from game import singleton_game
    print('O Rei ficou bravo, e quis batalhar com você!')
    king = Entity('👑🧝‍♂️',400,25)
    battle = Battle(king,singleton_game.player)
    if battle.result():
      print('Você conseguiu derrotar o Rei!')
      sleep(0.5)
      print('Ele então decide lhe nominar o Rei dos Elfos!')
      sleep(0.5)
      print('Você sai correndo, pois ninguém merece tal responsabilidade!')
      singleton_game.change_scene_to(StartScene2())

