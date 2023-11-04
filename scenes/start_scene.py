from battle import Battle
from entity import Entity
from items import mage_chest_key_item
from scenes.mage_house_scene import MageHouseScene
from scenes.moon_scene import MoonScene
from scenes.scene import Scene


class StartScene(Scene):

  def __init__(self):
    super().__init__(
        name='Floresta Encantada!',
        description='Você se encontra numa floresta, mas ao seu redor tem um fantasminha!!!',
        choices={
            'Fingir de morto': self.play_death,
            'Enfrentar o fantasma': self.battle_ghost,
        })

  def play_death(self):
    from game import singleton_game
    print('Você fingiu de morto e ele foi embora!!!')
    print('Você encontra uma espaço nave prestes a partir!')
    print('Você então decide ir em direção à lua.')
    singleton_game.change_scene_to(MoonScene())

  
  def battle_ghost(self):
    from game import singleton_game
    ghost = Entity('👻', 100, 30)
    ghost.add_item(mage_chest_key_item())
    battle = Battle(ghost, singleton_game.player)
    if battle.result():
      singleton_game.change_scene_to(MageHouseScene())
    else:
      singleton_game.lost_game = True

