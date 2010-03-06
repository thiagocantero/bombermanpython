import pygame
from constants import *
MONSTERS = dict()
MONSTERS['Monster01'] = {'sprites':('imagem/monsters/monster01.png',(3,3,3,3)),'moviments':[R,R,U,U,D,D,D,D,U,U,R,R,L,L,L,L],'velocity':(2,2)}
MONSTERS['Monster02'] = {'sprites':('imagem/monsters/monster02.png',(4,6,4,6)),'moviments':[L,L,L,R,R,R,R,R,R,L,L,L],'velocity':(2,2)}
MONSTERS['Monster03'] = {'sprites':('imagem/monsters/monster03.png',(4,4,6,4)),'moviments':[D,U,R,R,R,R,L,L,L,L],'velocity':(2,2)}
MONSTERS['Monster04'] = {'sprites':('imagem/monsters/monster02.png',(4,6,4,6)),'moviments':[R,R,U,U,D,D,D,D,U,U,R,R,L,L,L,L],'velocity':(2,2)}

class Monster :
    def __init__(self,monster_name,screen_position=(0,0)):
        self.__sprites = MONSTERS[monster_name]['sprites']
        self.__moviments = MONSTERS[monster_name]['moviments']
        self.__velocity = MONSTERS[monster_name]['velocity']
        self.sprites = self.__loadSprites__()
        self.moviments = self.__moviments
        self.velocity = self.__velocity
        self.current_moviment = 0
        self.direction = self.moviments[self.current_moviment]
        self.index_sprite = 0
        self.screen_position = screen_position
        self.is_moving = True

    def __loadSprites__(self) :
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
        
        if axis == AXIS_X :
            x += mult * self.velocity[0]
            pos = x
            width_height = SPRITE_W
        elif axis == AXIS_Y :
            y += mult * self.velocity[1]
            pos = y
            width_height = SPRITE_H
        
        if pos % width_height == 0 :
            self.is_moving = False
            self.current_moviment += 1
            self.current_moviment %= len(self.moviments)
            self.direction = self.moviments[self.current_moviment]
            
        self.index_sprite += 1
        self.index_sprite %= len(self.sprites[self.direction])          
            
        self.screen_position = (x,y)
        
        
    def move(self) :
        if self.direction == U :
            self.__updateAttr__(AXIS_Y, -1)
                
        elif self.direction == R :
            self.__updateAttr__(AXIS_X, 1)
                            
        elif self.direction == D :
            self.__updateAttr__(AXIS_Y, 1)
                
        elif self.direction == L :
            self.__updateAttr__(AXIS_X, -1)
        
    def paint(self,screen) :
        screen.blit(self.sprites[self.direction][self.index_sprite],self.screen_position)