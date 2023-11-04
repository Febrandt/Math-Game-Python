from item import item

from time import sleep
from battle import Battle
from entity import Entity
from items import mage_chest_key_item
from scenes.elf_king_scene import ElfKingScene
from scenes.scene import Scene


class ElfCityScene(Scene):

  def __init__(self):
    super().__init__(name='Cidade dos Elfos',
                     description='Você Chegou na cidade dos elfos, localizada dentro da cachoeira dourada, a cidade é completa de ouro, desde as casas até as privadas!',
                     choices={
                         'Conhecer o Rei': self.meet_king,
                         'batalhar com um porco': self.pig,
                         'Roubar ouro': self.steal
                     })

  def meet_king(self):
    from game import singleton_game
    singleton_game.change_scene_to(ElfKingScene())

  def steal(self):
    from game import singleton_game

    print('Você rouba o ouro')
    sleep(0.5)
    print('Já esperava ser atacado por elfos!')
    elfs = Entity('🧝‍♂️🧝‍♂️🧝‍♂️',150,60)
    battle = Battle(elfs,singleton_game.player)

    if battle.result():
      print('Você conseguiu roubar o ouro')
      sleep(0.5)
      print('Mas do Que adianta ganhar o bem material se o coração é fraco!')
      sleep(1)
      singleton_game.change_scene_to(ElfCityScene())
    else:
      print('Você Morreu!')
      singleton_game.lost_game = True

  def pig(self):
    from game import singleton_game

    pig = Entity('🐷',30,10)
    battle = Battle(pig,singleton_game.player)
    if battle.result():
      print('Você treinou sua força (+10 força)')
      singleton_game.player.damage += 10
    else:
      print('Como Você consegue perder para um porquinho????')
      singleton_game.lost_game = True