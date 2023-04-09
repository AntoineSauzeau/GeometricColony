import pygame
import time
import tkinter as tk
from tkinter import filedialog
import room as roomM
import tileset as tilesetM
from enum import IntEnum

class Direction(IntEnum):
    LEFT=0
    RIGHT=1,
    UP=2,
    DOWN=3

BLACK = (0, 0, 0)

N_TILESET_CASE_X = 7
N_TILEMAP_CASE_X = 20
N_CASE_Y = 20
TILESET_PART_WIDTH=N_TILESET_CASE_X*tilesetM.SPRITE_SIZE
TILEMAP_PART_WIDTH=N_TILEMAP_CASE_X*tilesetM.SPRITE_SIZE
HEADER_HEIGHT=50
WINDOW_WIDTH=TILEMAP_PART_WIDTH+3+TILESET_PART_WIDTH
WINDOW_HEIGHT=HEADER_HEIGHT+N_CASE_Y*tilesetM.SPRITE_SIZE

running = True
tilesetIndex = 0
tilesetScrollIndex = 0
cameraX = 0
cameraY = 0
spriteSelected = None

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tilemap maker")
font_35 = pygame.font.SysFont(None, 35)
font_28 = pygame.font.SysFont(None, 28)

root = tk.Tk()
root.withdraw()

room = None

def MouseOnWindow(x, y):
    return x > 0 and x < WINDOW_WIDTH-1 and y > HEADER_HEIGHT and y < WINDOW_HEIGHT-1

def MouseInTilemapPart(x, y):
    return x < TILEMAP_PART_WIDTH and MouseOnWindow(x, y)
    
def MouseInTilesetPart(x, y):
    return x >= TILEMAP_PART_WIDTH and MouseOnWindow(x, y)

def AddTileset():
    filePath = filedialog.askopenfilename()
    if filePath == None:
        return
    room.tilemap.AddTileset(filePath)
    print(filePath)

def Save():
    filePath = filedialog.asksaveasfilename()
    if filePath == None:
        return
    room.Save(filePath)

def LoadRoomFromFile():
    global room

    filePath = filedialog.askopenfilename()
    if filePath == '':
        return
    room = roomM.LoadFromFile(filePath)
    print(filePath)

def CreateNewRoom():
    global room

    name = input("Name : ")
    width = int(input("Width : "))
    height = int(input("Height : "))
    room = roomM.Room(name, width, height)

def MoveCamera(dir):
    global cameraX
    global cameraY

    if(dir == Direction.LEFT and cameraX-1>=0):
        cameraX -= 1
    elif(dir == Direction.RIGHT and cameraX+N_TILEMAP_CASE_X <= room.tilemap.width):
        cameraX += 1
    elif(dir == Direction.UP and cameraY-1 >= 0):
        cameraY -= 1
    elif(dir == Direction.DOWN and cameraY+N_CASE_Y <= room.tilemap.height):
        cameraY += 1

def ScrollTileset():
    pass

def MouseButtonUp(event):

    if room == None or not(MouseOnWindow(event.pos[0], event.pos[1])):
        return

    global spriteSelected

    if(MouseInTilesetPart(event.pos[0], event.pos[1])):
        caseX = (event.pos[0] - TILEMAP_PART_WIDTH) // tilesetM.SPRITE_SIZE
        caseY = (event.pos[1] - HEADER_HEIGHT) // tilesetM.SPRITE_SIZE

    elif(MouseInTilemapPart(event.pos[0], event.pos[1])):
        caseX = event.pos[0] // tilesetM.SPRITE_SIZE
        caseY = (event.pos[1] - HEADER_HEIGHT) // tilesetM.SPRITE_SIZE

        if(caseX >= room.tilemap.width or caseY >= room.tilemap.height):
            return
    
    if event.button == pygame.BUTTON_LEFT:
        if(MouseInTilesetPart(event.pos[0], event.pos[1])):
            spriteIndex = caseY * N_TILESET_CASE_X + caseX
            spriteSelected = (spriteIndex, tilesetIndex)
            print(spriteSelected)
        elif MouseInTilemapPart(event.pos[0], event.pos[1]):
            if spriteSelected != None:
                print(room.tilemap.array[caseY][caseX])
                room.tilemap.array[caseY][caseX] = spriteSelected

    elif event.button == pygame.BUTTON_RIGHT:
        if MouseInTilemapPart(event.pos[0], event.pos[1]):
            room.tilemap.array[caseY][caseX] = (-1, -1)

    elif event.button == pygame.BUTTON_MIDDLE:
        if MouseInTilemapPart(event.pos[0], event.pos[1]):
            spriteSelected = room.tilemap.array[caseY][caseX]

    elif event.button == pygame.BUTTON_RIGHT:
        pass

def KeyDownTilemap(event):
    print("Tilemap")

def KeyDownTileset(event):
    print("Tileset")

def KeyDown(event):

    if event.key == pygame.K_l:
        LoadRoomFromFile()
    if event.key == pygame.K_r:
        CreateNewRoom()

    if room != None:
        if event.key == pygame.K_s:
            Save()
        elif event.key == pygame.K_t:
            AddTileset()
        elif event.key == pygame.K_z:
            MoveCamera(Direction.UP)
        elif event.key == pygame.K_s:
            MoveCamera(Direction.DOWN)
        elif event.key == pygame.K_q:
            MoveCamera(Direction.LEFT)
        elif event.key == pygame.K_d:
            MoveCamera(Direction.RIGHT)    

    mousePos = pygame.mouse.get_pos()
    print(mousePos)
    if MouseInTilemapPart(mousePos[0], mousePos[1]):
        KeyDownTilemap(event)
    elif MouseInTilesetPart(mousePos[0], mousePos[1]):
        KeyDownTileset(event)

def DrawTilemap():

    tilesets = room.tilemap.tilesets
    for l in range(room.tilemap.height):
        for c in range(room.tilemap.width):
            (spriteIndex, spriteTilesetIndex) = room.tilemap.array[l][c]

            if(spriteTilesetIndex >= len(tilesets) or spriteIndex == -1):
                continue

            lSprite = tilesets[spriteTilesetIndex].lSprite
            if spriteIndex < len(lSprite):
                screen.blit(lSprite[spriteIndex], ((cameraX + c) * tilesetM.SPRITE_SIZE, (cameraY+l) * tilesetM.SPRITE_SIZE + HEADER_HEIGHT))
    
    for l in range(N_CASE_Y):
        for c in range(N_TILEMAP_CASE_X):
            pygame.draw.rect(screen, BLACK, (c * tilesetM.SPRITE_SIZE, l * tilesetM.SPRITE_SIZE + HEADER_HEIGHT, tilesetM.SPRITE_SIZE, tilesetM.SPRITE_SIZE), 1)


def DrawTileset():
    if(len(room.tilemap.tilesets) == 0):
        return 

    usedTileset = room.tilemap.tilesets[tilesetIndex]
    firstSpriteIndex = tilesetScrollIndex*N_TILESET_CASE_X
    for i in range(firstSpriteIndex, min(len(usedTileset.lSprite), firstSpriteIndex+N_CASE_Y*N_TILESET_CASE_X)):
         
        xI = i % N_TILESET_CASE_X
        yI = i // N_TILESET_CASE_X
        x = TILEMAP_PART_WIDTH + xI * tilesetM.SPRITE_SIZE + 3
        y = yI * tilesetM.SPRITE_SIZE + HEADER_HEIGHT

        sprite = usedTileset.lSprite[i]
        screen.blit(sprite, (x, y, tilesetM.SPRITE_SIZE, tilesetM.SPRITE_SIZE))

def DrawHeader():
    textRoomName = font_28.render(room.name, True, BLACK)
    screen.blit(textRoomName, (10, 17))

def Draw():
    screen.fill((255, 255, 255))

    if(room != None):
        DrawTilemap()
        DrawTileset()
        DrawHeader()
    else:
        text = font_35.render("Keys", True, BLACK)
        screen.blit(text, (WINDOW_WIDTH/2 - text.get_width()/2, 120))
        text = font_28.render("R : Create a new room", True, BLACK)
        screen.blit(text, (WINDOW_WIDTH/2 - text.get_width()/2, 150))
        text = font_28.render("L : Load an existent room", True, BLACK)
        screen.blit(text, (WINDOW_WIDTH/2 - text.get_width()/2, 180))
        text = font_28.render("S : Save the current room", True, BLACK)
        screen.blit(text, (WINDOW_WIDTH/2 - text.get_width()/2, 210))
        text = font_28.render("T : Add a tileset", True, BLACK)
        screen.blit(text, (WINDOW_WIDTH/2 - text.get_width()/2, 240))

    pygame.display.update()

while running:

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        elif(event.type == pygame.MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            MouseButtonUp(event)
        elif(event.type == pygame.KEYDOWN):
            KeyDown(event)

        Draw()

    time.sleep(0.1)
