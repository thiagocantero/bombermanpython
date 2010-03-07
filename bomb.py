import pygame
from pygame.locals import *
from pygame import Rect

from constants import *
from datetime import datetime

WAITING = 0
DESTROYING = 1
FINISHED = 2

class Bomb:

    def __init__(self, matrix_position) :
        self.__sprites = ['imagem/bomb.png', (5,1)]
        self.sprites = self.__loadSprites__()
        self.screen_position = matrixToScreen(matrix_position[0],matrix_position[1])
        self.start_time = datetime.now()
        self.duration_time = 5
        self.index_sprite = 0
        self.status = WAITING
        self.__range = 1
        self.max_range = 1
        
    def __loadSprites__(self) :
        sprites_image_filename = self.__sprites[0]
        sprites_image_quantity = self.__sprites[1]
        
        sprites_image = pygame.image.load(sprites_image_filename).convert_alpha()
        sprites = {WAITING:list(), DESTROYING:list()}
        
        tot = 0
        for i in range(0,sprites_image_quantity[0]) :
            sprites[WAITING].append(sprites_image.subsurface(pygame.Rect(i*SPRITE_W,0,SPRITE_W,SPRITE_H)))
        tot += sprites_image_quantity[0]
        for i in range(0,sprites_image_quantity[1]) :
            sprites[DESTROYING].append(sprites_image.subsurface(pygame.Rect((i+tot)*SPRITE_W,0,SPRITE_W,SPRITE_H)))
        tot += sprites_image_quantity[1]
        
        return sprites
        
    def process(self):
        if self.status == WAITING :
            now = datetime.now()
            dif_time = now - self.start_time
            if dif_time.seconds >= self.duration_time :
                self.status = DESTROYING
        elif self.status == DESTROYING :
            print "Explodi!"
            self.status = FINISHED

        if self.status <> FINISHED :
            self.index_sprite += 1
            self.index_sprite %= len(self.sprites[self.status])            
        
    def paint(self, screen) :
        screen.blit(self.sprites[self.status][self.index_sprite], self.screen_position)
        
    def isFinished(self) :
        return (self.status == FINISHED)