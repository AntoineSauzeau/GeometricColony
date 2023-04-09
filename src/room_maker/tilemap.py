
from tileset import Tileset
import array as arrayM


class Tilemap:

    def __init__(self, width, height):         #Crée avec width en parametree
        self.tilesets = []
        self.width = width
        self.height = height

        self.array = [[ (-1, -1) for y in range(height)] for x in range(width)]

    def AddTileset(self, name):
        tileset = Tileset(name)
        self.tilesets.append(tileset)

