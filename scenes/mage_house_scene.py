
from battle import Battle
from entity import Entity
from scenes.scene import Scene
from scenes.mage_chest_scene import MageChestScene

class MageHouseScene(Scene):

  def __init__(self):
    super().__init__(
        name='casa do Mago!!!',
        description='O mago está quente! Corra desse tarado!',
        choices={
            'Lutar com o mago': self.fight_mage,
            'Correr': self.run,
        })


  def fight_mage(self):
    from game import singleton_game
    mage = Entity('🧙‍♂️', 200, 30)
    battle = Battle(mage, singleton_game.player)
    if battle.result():
      singleton_game.change_scene_to(MageChestScene())
    else:
      singleton_game.lost_game = True


  def run(self):
    from game import singleton_game
    print('Você Correu????')
    print('Seu fracote!!!')
    print('Você vai lutar contra o Deus da Ordem AGORA!!!')
    deus = Entity('☀',300,40)
    battle = Battle(deus,singleton_game.player)
    if battle.result():
      print('Você é o novo Deus, parabéns!!!')
      print('Você Ganhou o Jogo!!!!')
      singleton_game.winned_game = True
    else:
      singleton_game.lost_game = True
