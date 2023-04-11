import json
import pickle
from tilemap import Tilemap
from tileset import Tileset

class Room:

    def __init__(self, name, width, height):
        self.tilemap = Tilemap(width, height)
        self.tilesets = []
        self.name = name
        self.spawnPos = (0, 0)

    def Save(self, filePath):
        data = {}

        data["name"] = self.name
        data["width"] = self.tilemap.width
        data["height"] = self.tilemap.width
        
        lTilesetName = []
        for tileset in self.tilemap.tilesets:
            lTilesetName.append(tileset.name)

        data["tilesets"] = lTilesetName
        data["tilemap"] = self.tilemap.array

        file = open(filePath, "w")
        file.write(str(data))

        file.close()

    def AddTileset(self, filename):
        self.tilesets.append(Tileset(filename))
    
def LoadFromFile(path):
    file = open(path, "r")
    content = json.load(file)
    print(content)

    room = Room(content["name"], content["width"], content["height"])

    for tilesetName in content["tilesets"]:
        room.AddTileset(tilesetName)

    room.tilemap.array = content["tilemap"]

    return room

    


