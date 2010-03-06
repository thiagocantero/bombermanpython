import pygame
from pygame.locals import *
from pygame import Rect
from constants import *

class Bomberman:
    def __init__(self):
        self.__sprites = ['imagem/bomberman.png', (3,3,3,3)]
        self.sprites = self.__loadSprites__()
        self.index_moviment = 0
        self.velocity = 2
        self.direction = D
        self.screen_position = (32,32)
        self.index_sprite = 0
        self.is_moving = False 
        self.items = []    

    def __loadSprites__(self):
        sprites_image_filename = self.__sprites[0]
        sprites_image_quantity = self.__sprites[1]
        
        sprites_image = pygame.image.load(sprites_image_filename).convert_alpha()
        sprites = {U:list(), R:list(), D:list(), L:list()}
        
        tot = 0
        for i in range(0,sprites_image_quantity[0]) :
            sprites[U].append(sprites_image.subsurface(pygame.Rect(i*SPRITE_W,0,SPRITE_W,SPRITE_H)))
        tot += sprites_image_quantity[0]
        for i in range(0,sprites_image_quantity[1]) :
            sprites[R].append(sprites_image.subsurface(pygame.Rect((i+tot)*SPRITE_W,0,SPRITE_W,SPRITE_H)))
        tot += sprites_image_quantity[1]
        for i in range(0,sprites_image_quantity[2]) :
            sprites[D].append(sprites_image.subsurface(pygame.Rect((i+tot)*SPRITE_W,0,SPRITE_W,SPRITE_H)))
        tot += sprites_image_quantity[2]
        for i in range(0,sprites_image_quantity[3]) :
            sprites[L].append(sprites_image.subsurface(pygame.Rect((i+tot)*SPRITE_W,0,SPRITE_W,SPRITE_H)))            
        tot += sprites_image_quantity[3]
        
        return sprites


    def  __updateAttr__(self, axis, mult):
        x, y = self.screen_position
        self.is_moving = True
        
        if axis == AXIS_X :
            x += mult * self.velocity
            pos = x
            width_height = SPRITE_W
        elif axis == AXIS_Y :
            y += mult * self.velocity
            pos = y
            width_height = SPRITE_H
        
        self.index_sprite += 1
        self.index_sprite %= len(self.sprites[self.direction])   
        
        if pos % width_height == 0 :
            self.is_moving = False
            self.index_sprite = 0
            
        self.screen_position = (x,y)
        

    def process(self):
        pressed = pygame.key.get_pressed()
        
        x,y = self.screen_position
        
        if self.is_moving:
            if self.direction == U:
                self.__updateAttr__(AXIS_Y, -1)
            elif self.direction == D:
                self.__updateAttr__(AXIS_Y, 1)
            elif self.direction == R:
                self.__updateAttr__(AXIS_X, 1)
            elif self.direction == L:
                self.__updateAttr__(AXIS_X, -1)
        else:
			if pressed[K_UP]:
				self.direction = U
				self.__updateAttr__(AXIS_Y, -1)
			elif pressed[K_DOWN]:
				self.direction = D
				self.__updateAttr__(AXIS_Y, 1)
			elif pressed[K_RIGHT]:
				self.direction = R
				self.__updateAttr__(AXIS_X, 1)
			elif pressed[K_LEFT]:
				self.direction = L
				self.__updateAttr__(AXIS_X, -1)
        
        if pressed[K_SPACE]:
            self.__setBomb__()
        
    def tryItens(self):
        for item in self.items
            if item.tryFinish():
                self.items.remove(item)
        
    def paint(self,screen) :
        screen.blit(self.sprites[self.direction][self.index_sprite],self.screen_position)

    def __setBomb__(self):
        print 'Boooomba!!'
