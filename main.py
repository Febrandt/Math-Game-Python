from game import singleton_game
from scenes.start_scene import StartScene
from scenes.waterfall_scene import WaterfallScene

singleton_game.change_scene_to(StartScene())
singleton_game.game_loop()
