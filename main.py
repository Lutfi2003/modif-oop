import pygame
from oop.bullets.arrow import Arrow
from oop.bullets.fire import Fire
from oop.bullets.stone import Stone
from oop.bullets.spear import Spear
from oop.control import GameController
from oop.scene import Scene
from oop.levels.level1 import Level1
from oop.levels.level2 import Level2
from oop.levels.level3 import Level3
from oop.levels.level4 import Level4
from oop.levels.level5 import Level5
from oop.levels.level6 import Level6
from oop.player import Player

pygame.init()

scene = Scene((640, 480))
scene.setup_level(
  Level1,
  Level2,
  Level3,
  Level4,
  Level5,
  Level6,
)

player = Player(scene, Stone())
game_controller = GameController(player)

running = True

while(running):
  scene.fill()
  game_controller.keyboard_event()
  game_controller.mouse_position_event()
  pygame.display.flip()