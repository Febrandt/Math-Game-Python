
from battle import Battle
from entity import Entity
from items import mage_chest_key_item
from scenes.scene import Scene
from scenes.waterfall_scene import WaterfallScene

class MageChestScene(Scene):

  def __init__(self):
    super().__init__(name='Baú do Mágico!',
                     description='Só Deus sabe o que tem dentro desse baú',
                     choices={
                         'Abrir Baú': self.open_chest,
                         'Não Abrir Baú': self.not_open_chest,
                     })

  def open_chest(self):
    from game import singleton_game

    if mage_chest_key_item() in singleton_game.player.inventory:
      print('Você abriu o baú e ganhou 10 de força!')
      singleton_game.player.inventory.remove(mage_chest_key_item())
      singleton_game.player.damage += 10
    else:
      print('Você não tem a chave para abrir o baú!')
      self.not_open_chest()

  def not_open_chest(self):
    from game import singleton_game

    print('Você não abriu o baú!!!')
    print('Continue sua Jornada.')
    singleton_game.change_scene_to(WaterfallScene())
