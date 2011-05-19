# Bomberman game
# Author: Bruna Xavier
# Creation date: 04-30-2011

class World(object):
    def __init__(self, map, player):
        self.map = map
        self.player = player
    
    
import pygame
from map import PygameMap
from player import PygamePlayer
from bomb import PygameBomb, PygameBombModel

class PygameWorld(World):
    
    def __init__(self, screen):
        super(PygameWorld, self).__init__(PygameMap([0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0, 0, 0, 0, 0, 0], 5, 5, screen, 'images/destructible_box.png', 'images/undestructible_box.png', 'images/rewards.png', tiles_width=32, tiles_height=32, ublocks=[0], dblocks={0:3}, rewards={0:1}, forbidden_positions_dblocks=[(1, 1), (1, 2), (2, 1), (2, 2)]), PygamePlayer(screen, (32, 32), 'images/bomberman.png', tiles_width=32, tiles_height=32))
        
        self.__screen = screen
        self.bomb_model = PygameBombModel('images/bomb.png', 'images/explosion.png', tiles_width=32, tiles_height=32)
        self.bombs = []
        
    def run(self):
        if self.__player_can_walk():
            self.player.walk()
        else:
            self.player.cancel_movement()
        
    def draw(self):
        self.map.draw()

        for bomb in self.bombs:
            bomb.draw()
            
        self.player.draw()
        
    def __player_can_place_bomb(self):
        col, row = self.player.position
        
        if self.map.has_nothing(row, col):
            if self.player.max_bombs > 0:
                return True
            
        return False
        
    def __player_can_walk(self):
        col, row = self.player.position
        if 0 > row or row > self.map.height :
            return False
        
        if 0 > col or col > self.map.width :
            return False
        
        if self.map.has_nothing(row, col):
            return True
            
        if self.map.has_ublock(row, col) or self.map.has_dblock(row, col):
            return False
            
        if self.map.has_reward(row, col):
            print "GET REWARD!!", self.map.get_reward(row, col)
            self.map.destroy_reward(row, col)
            return True
            
    def place_bomb(self):
        if self.__player_can_place_bomb():
            self.player.max_bombs -= 1
            bomb = PygameBomb(self.__screen, self.bomb_model, self.player.position, 1)
            self.bombs.append(bomb)
            
            print self.player.position
            