import json
import pickle
from tilemap import Tilemap

class Room:

    def __init__(self, name, width, height):
        self.tilemap = Tilemap(width, height)
        self.name = name

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
    
def LoadFromFile(path):
    file = open(path, "r")
    content = json.load(file)
    print(content)

    room = Room(content["name"], content["width"], content["height"])

    for tilesetName in content["tilesets"]:
        room.tilemap.AddTileset(tilesetName)

    room.tilemap.array = content["tilemap"]

    return room


