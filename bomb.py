# Bomberman game
# Author: Bruna Xavier
# Creation date: 05-19-2011

class Bomb(object):
    
    def __init__(self, position, range):
        self.position = position
        self.range = range

import pygame
class PygameBombModel:

    def __init__(self, bomb_image, explosion_image, tiles=1, tiles_per_direction=1, tiles_width=16, tiles_height=16):
        self.__bomb_image = pygame.image.load(bomb_image).convert_alpha()        
        self.__explosion_image = pygame.image.load(explosion_image).convert_alpha()        
        
        self.tiles=1
        self.tiles_per_direction = tiles_per_direction
        self.tiles_width = tiles_width
        self.tiles_height = tiles_height
        
        # North , East, South, West, Center
        self.bomb_tiles = []
        for i in range(self.tiles):
            self.bomb_tiles.append(self.__load_bomb_image(i))
            
        self.explosion_tiles = [self.__load_explosion_image(0), self.__load_explosion_image(1), self.__load_explosion_image(2), self.__load_explosion_image(3), self.__load_explosion_image(4, 1)]
        
    def __load_bomb_image(self, i):
        x, y = (self.tiles_width * i, 0)
        w, h = (self.tiles_width, self.tiles_height)
        rect = pygame.Rect(x, y, w, h)
            
        return self.__bomb_image.subsurface(rect)
        
    def __load_explosion_image(self, start, tiles=None):
        if tiles == None:
            tiles = self.tiles_per_direction
            
        images = list()
        for i in xrange(start, start + tiles):
            x, y = (self.tiles_width * i, 0)
            w, h = (self.tiles_width, self.tiles_height)
            rect = pygame.Rect(x, y, w, h)
            
            images.append(self.__explosion_image.subsurface(rect))
            
        return images
        
import pygame
class PygameBomb(Bomb):
    
    READY_TO_EXPLODE    =   1
    WAITING_ACTIVATION  =   2
    EXPLODING           =   3
    
    def __init__(self, screen, model, position, range):
        super(PygameBomb, self).__init__(position, range)
        self.__screen = screen
        self.__screen_position = (position[0] * model.tiles_width, position[1] * model.tiles_height)
        self.__model = model
        
        self.__status = self.READY_TO_EXPLODE
        self.__current_tile = 0
        
    def __change_status(self):
        # TODO acrescentar o modo de controle remoto
        if self.__status == self.READY_TO_EXPLODE:
            self.__status = self.EXPLODING
            self.__current_tile = 0
        
    def draw(self):
        # TODO acrescentar o modo de controle remoto
        if self.__status == self.READY_TO_EXPLODE:
            tile = self.__model.bomb_tiles[self.__current_tile]
            self.__current_tile = (self.__current_tile + 1) % self.__model.tiles
            self.__screen.blit(tile, self.__screen_position)