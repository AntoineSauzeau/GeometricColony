import pygame
import tile
from pathlib import Path

BASE_SPRITE_SIZE = 16
SCALE_FACTOR = 2
SPRITE_SIZE = SCALE_FACTOR * BASE_SPRITE_SIZE

class Tileset:

    def __init__(self, name):
        self.name = name

        self.lSprite = []
        self.tilesetImage = pygame.image.load(Path("assets/tilesets", name))
        for xI in range(self.tilesetImage.get_width() // BASE_SPRITE_SIZE):
            for yI in range(self.tilesetImage.get_height() // BASE_SPRITE_SIZE):
                spriteImageRect = pygame.Rect(xI*BASE_SPRITE_SIZE, yI*BASE_SPRITE_SIZE, BASE_SPRITE_SIZE, BASE_SPRITE_SIZE)
                spriteImage = self.tilesetImage.subsurface(spriteImageRect)
                spriteImage = pygame.transform.scale_by(spriteImage, SCALE_FACTOR)
                #newTile = tile.Tile(spriteImage, xI, yI)
                self.lSprite.append(spriteImage)
