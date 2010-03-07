S = 0
U = 1
R = 2
D = 3
L = 4

FPS = 12

SCREEN_W = 512
SCREEN_H = 512

SCENARIO_W = 16
SCENARIO_H = 16

SPRITE_W = 32
SPRITE_H = 32

AXIS_X = 1
AXIS_Y = 2

SPRITE_VEL_X = 2
SPRITE_VEL_Y = 2

GROUND = 0
UNDEST_BOX = 1
DEST_BOX = 2
BOMBERMAN = 3
MONSTER = 4
MONSTER_ROUTE = 5
BOMB = 6
EXPLOSION = 7

ITEM_VELOCITY = 10


def arrayToMatrix(pos) :
    x = pos % SCENARIO_W
    y = pos / SCENARIO_H
    return (x, y)
    
def matrixToArray(x, y) :
    return y * SCENARIO_W + x

def matrixToScreen(x, y) :
    return (x*SPRITE_W, y*SPRITE_H)
    
def screenToMatrix(x, y) :
    return (x//SPRITE_W, y//SPRITE_H)
    
def arrayToScreen(pos) :
    x, y = arrayToMatrix(pos)
    return matrixToScreen(x, y)
    
def screenToArray(x, y) :
    screenToMatrix(x, y)
    return matrixToArray(x, y)    
    