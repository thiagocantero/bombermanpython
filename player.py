# Bomberman game
# Author: Bruna Xavier
# Creation date: 04-30-2011

class Player(object):
    
    def __init__(self):
        # lives
        self.life = 3
        
        # if player is walking (if it is trying to align to grid)
        self.walking = False
        
        # virtual position
        self.position = (1, 1)
        
        # direction of movement
        self.direction = (1, 0)
        
        # speed
        self.speed = (4, 4)
        
    def update_position(self):        
        x, y = self.position
        dx, dy = self.direction
        self.position = x+dx, y+dy
        
    def cancel_movement(self):
        x, y = self.position
        dx, dy = self.direction
        self.position = x-dx, y-dy
        self.walking = False
        
    def change_direction(self, other):
        if not self.walking:
            self.direction = other
            self.update_position()
            self.walking = True
        
import pygame
class PygamePlayer(Player):

    NORTH   =   (0, -1)
    SOUTH   =   (0, 1)
    RIGHT   =   (1, 0)
    LEFT    =   (-1, 0)
    
    def __init__(self, screen, screen_position, player_image, tiles_per_direction=3, tiles_width=16, tiles_height=16):
        super(PygamePlayer, self).__init__()

        self.__screen = screen
        self.__screen_position = screen_position
        self.__player_image = pygame.image.load(player_image).convert_alpha()        
        
        self.__tiles_per_direction = tiles_per_direction
        self.__tiles_width = tiles_width
        self.__tiles_height = tiles_height

        self.tiles = {self.NORTH: self.__load_image(0), self.SOUTH: self.__load_image(6), self.RIGHT: self.__load_image(3), self.LEFT: self.__load_image(9)}
        self.current_tile = 0
        
    def __load_image(self, start):
        images = list()
        for i in xrange(start, start + self.__tiles_per_direction):
            x, y = (self.__tiles_width * i, 0)
            w, h = (self.__tiles_width, self.__tiles_height)
            rect = pygame.Rect(x, y, w, h)
            
            print x, y, w, h
            
            images.append(self.__player_image.subsurface(rect))
            
        return images
        
    def walk(self):
        if not self.walking:
            # stay in this position if not walking
            self.current_tile = 0
            return
            
        # final position
        fx, fy = self.position
        fx, fy = fx * self.__tiles_height, fy * self.__tiles_width
        
        # move toward self.direction with speed self.speed
        dx, dy = self.speed[0] * self.direction[0], self.speed[1] * self.direction[1]
        x, y = self.__screen_position
        x, y = x + dx, y + dy
        
        # stop walking if player is horizontally align with grid
        if abs(fx - x) < abs(dx):
            x = fx
            self.walking = False
            print "PLAYER AT", (y, x)
            print "POSITION", (self.position[1], self.position[0])
        
        # stop walking if player is vertically align with grid        
        if abs(fy - y) < abs(dy):
            y = fy
            self.walking = False
            print "PLAYER AT", (y, x)
            print "POSITION", (self.position[1], self.position[0])
            
        # update screen position
        self.__screen_position = x, y
        
        # update tile
        self.current_tile = (self.current_tile + 1) % self.__tiles_per_direction
        
    def draw(self):
        tile = self.tiles[self.direction][self.current_tile]
        self.__screen.blit(tile, self.__screen_position)
        