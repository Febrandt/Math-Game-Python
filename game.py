from os import system
from typing import Optional

from entity import Entity
from scenes.scene import Scene
from scenes.start_scene import StartScene


singleton_wins = 3
singleton_guess = 3

class Game:

  def __init__(self) -> None:
    self.choose_difficulty()
    self.player = self.choose_player()
    self.current_scene: Optional[Scene] = None
    self.scenes = {}
    self.lost_game = False
    self.winned_game = False

  def choose_difficulty(self):
    global singleton_wins, singleton_guess

    print('--- DIFICULDADE ----')
    print('0. GUGU GAGA 👶🍼')
    print('1. Normal 😐')
    print('3. VEM!!! 👿')
    match int(input('Escolha a dificuldade: ')):
      case 0:
        singleton_wins = 4
        singleton_guess = 2
      case 1:
        singleton_wins = 3
        singleton_guess = 3
      case 2:
        singleton_wins = 2
        singleton_guess = 4
        
  
  def choose_player(self):
    print('0. Guerreiro - (80 vida, 50 dano)')
    print('1. Arqueiro - (120 vida, 40 dano)')
    print('2. Bruxa - (50 vida, 70 dano)')
    choose = int(input('Escolha um personagem: '))
    match choose:
      case 0:
        return Entity('⚔👨',80,50)
      case 1:
        return Entity('🏹👨',120,40)
      case 2:
        return Entity('🧹👩',50,70)
        
  
  def change_scene_to(self,scene: Scene):
    self.current_scene = scene

  def game_loop(self):
    print(f'Você é o player: {self.player.emoji}!')
                
    while self.current_scene != None and not self.lost_game and not self.winned_game:

      print()
      print('-'*5,'Cena: ' ,self.current_scene.name,'-'*5)
      print(self.current_scene.description)
      print()
      for index, key in enumerate(list(self.current_scene.choices.keys())):
        print(f'{index}. {key}')
      try:

        option = int(input('Escolha uma opção: '))
        system('cls||clear')

        list(self.current_scene.choices.items())[option][1]()

      
      except:
        self.lost_game = True
        print('Você escolheu uma opção errada! Volte para o começo!')
    
    if self.lost_game:
      print('Volte outra vez otário!!!')

    if self.winned_game:
      print('Parabéns você ganhou absolutamente nada jogando meu jogo!')



singleton_game = Game()