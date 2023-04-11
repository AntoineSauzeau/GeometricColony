import array as arrayM


class Tilemap:

    def __init__(self, width, height):         #Crée avec width en parametree
        self.width = width
        self.height = height

        self.array = [[ (-1, -1) for y in range(height)] for x in range(width)]


