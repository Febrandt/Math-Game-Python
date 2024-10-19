from items import mage_chest_key_item
from scenes.mage_house_scene import MageHouseScene
from scenes.scene import Scene
from battle import Battle
from entity import Entity



class MoonScene(Scene):

  def __init__(self):
    super().__init__(
        name='Lua!!!',
        description='O silêncio é ensurdecedor! O foguete ficou bravo contigo!',
        choices={
            'Lutar com o foguete': self.fight_rocket,
            'Pedir perdão por nada!': self.pardon,
        })


  def fight_rocket(self):
    from game import singleton_game
    rocket = Entity('🚀', 500, 10)
    rocket.add_item(mage_chest_key_item())
    battle = Battle(rocket, singleton_game.player)
    if battle.result():
      print('Você Então força o foguete a ir para casa do mago quente!')
      singleton_game.change_scene_to(MageHouseScene())
    else:
      singleton_game.lost_game = True
  
  def pardon(self):
    from game import singleton_game
    print('Você perdiu perdão e ele aceitou !')
    print('Ele te deu uma chave e te levou para o mago quente!')
    singleton_game.player.add_item(mage_chest_key_item())
    singleton_game.change_scene_to(MageHouseScene())
  