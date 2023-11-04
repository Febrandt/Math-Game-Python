from item import item

from time import sleep
from battle import Battle
from entity import Entity
from items import mage_chest_key_item
from scenes.scene import Scene
from scenes.elf_city_scene import ElfCityScene


class WaterfallScene(Scene):

  def __init__(self):
    super().__init__(name='Cachoeira Dourada',
                     description='Você Chegou na cachoeira Dourada, Aqui tudo é banhado à ouro!',
                     choices={
                         'Banhar-se': self.drown,
                         'Apreciar a vista': self.look,
                         'Roubar ouro': self.steal
                     })

  def drown(self):
    from game import singleton_game
    print('Enquanto você se banha, um dragão de komodo o ataca!')

    dragon = Entity('🐲',70,30)
    battle = Battle(dragon,singleton_game.player)
    if battle.result():
      print('Você ganhou do dragão!')
      sleep(0.5)
      print('Mas você não imaginava que a cidade dos elfos seria liberdata das desgraças desse ser')
      sleep(0.5)
      print('Você é convidado pelos elfos para sua cidade!')
      singleton_game.change_scene_to(ElfCityScene())


  def steal(self):
    from game import singleton_game

    print('Você rouba o ouro')
    sleep(0.5)
    print('Mas não esperava ser atacado por elfos!')
    elfs = Entity('🧝‍♂️🧝‍♂️🧝‍♂️',150,60)
    battle = Battle(elfs,singleton_game.player)

    if battle.result():
      print('Você conseguiu roubar o ouro')
      sleep(0.5)
      print('Mas do Que adianta ganhar o bem material se o coração é fraco!')
      sleep(1)
      singleton_game.change_scene_to(WaterfallScene())
    else:
      print('Você Morreu!')
      singleton_game.lost_game = True
  

  def look(self):
    from game import singleton_game

    print('Não olhe demais o ouro pode lhe cegar!')
    sleep(0.5)
    print('Disse o elfo, cuidador da cachoeira.')
    sleep(0.5)
    print('A conversa continua...')
    sleep(3)
    print('Ele te oferece uma estadia na cidade élfica, que se localiza dentro da cachoeira')
    sleep(1)
    choose = input('Você aceita? [s/n]').lower()
    if choose == 's':
      singleton_game.change_scene_to(ElfCityScene())
    else:
      print('Você fica em paz e volta para a cachoeira')
      singleton_game.change_scene_to(WaterfallScene())