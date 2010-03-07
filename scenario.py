import pygame
import random
from constants import *
from map import Map
from monster import Monster

class Scenario :
    '''Define o cenário da fase. Cenário inclui: mapa, itens, caixas destrutíveis e saída'''
    def __init__(self, map_name) :
        '''Construtor da classe Scenario'''
        self.map = Map(map_name)
        self.virtual_map = self.__createVirtualMap__()
        self.items = None
        self.exit = None
        self.monsters = self.__createMonsters__()
        
        
    def __createVirtualMap__(self) :
        return self.map.getMap()
        
        
    def __createMonsters__(self, quantity=3) :
        '''Cria quantity monstros em posições aleatórias'''
        monsters = list()
        r = random.Random()
        placed_monsters = 0
        while placed_monsters < quantity :
            tries = 5
            for i in range(0, tries) :
                x = int(r.random() * 1000) % SCENARIO_W
                y = int(r.random() * 1000) % SCENARIO_H
                
                pos_monster = None
                pos_route = list()
                
                m = Monster(self,'Monster01',(x*SPRITE_W, y*SPRITE_H))
                pos_monster = y * SCENARIO_W + x
                pos_route = m.makeRoute(x,y)
                
                hasException = False
                
                for (x_route, y_route) in pos_route :
                    try:
                        pos = matrixToArray(x_route,y_route)
                        if self.virtual_map[pos] == UNDEST_BOX :
                            raise Exception()
                        elif self.virtual_map[pos] == MONSTER :
                            raise Exception()  
                        elif self.virtual_map[pos] == MONSTER_ROUTE :
                            raise Exception()                        
                    except :
                        hasException = True
                        break;
                        
                if not hasException :
                    self.map.destroyBox(pos_monster)
                    for (x_route, y_route) in pos_route :
                        pos = matrixToArray(x_route,y_route)
                        self.virtual_map[pos] = MONSTER_ROUTE
                        self.map.destroyBox(pos)
                    self.virtual_map[pos_monster] = MONSTER

                    placed_monsters += 1
                    monsters.append(m)                    
                    break;
        return monsters
    
    
    def process(self):
        for monster in self.monsters :
            monster.process()
            
    def freeRoomBomberman(self,bomberman_pos):
        
        def setGround():
            array_pos = matrixToArray(matrix_pos_cruz[0],matrix_pos_cruz[1])
            if self.virtual_map[array_pos] != UNDEST_BOX:
                self.virtual_map[array_pos] = GROUND
            self.map.destroyBox(array_pos)
    
        matrix_pos = screenToMatrix(bomberman_pos[0],bomberman_pos[1])
        
        array_pos = matrixToArray(matrix_pos[0],matrix_pos[1])
        self.virtual_map[array_pos] = BOMBERMAN
        self.map.destroyBox(array_pos)
        
        #montando a cruz
        matrix_pos_cruz = (matrix_pos[0]-1,matrix_pos[1])        
        setGround()
        matrix_pos_cruz = (matrix_pos[0]+1,matrix_pos[1])
        setGround()
        matrix_pos_cruz = (matrix_pos[0],matrix_pos[1]-1)
        setGround()
        matrix_pos_cruz = (matrix_pos[0],matrix_pos[1]+1)
        setGround()
    
    def canMove(self, direction, entity):
        matrix_pos_current = screenToMatrix(entity.screen_position[0],entity.screen_position[1])
        array_pos_current = matrixToArray(matrix_pos_current[0],matrix_pos_current[1])
        
        if direction == U:
            matrix_pos_new = (matrix_pos_current[0],matrix_pos_current[1]-1)
        elif direction == D:
            matrix_pos_new = (matrix_pos_current[0],matrix_pos_current[1]+1)
        elif direction == R:
            matrix_pos_new = (matrix_pos_current[0]+1,matrix_pos_current[1])
        elif direction == L:
            matrix_pos_new = (matrix_pos_current[0]-1,matrix_pos_current[1])
    
        array_pos_new = matrixToArray(matrix_pos_new[0],matrix_pos_new[1])
        
        #print "I'm in: ","(",matrix_pos_current[0],",",matrix_pos_current[1],")"
        #print "I'm going to: ","(",matrix_pos_new[0],",",matrix_pos_new[1],")"
        #print "There's a ",self.virtual_map[array_pos_new]
        
        allow = False
        if self.virtual_map[array_pos_new] == GROUND or self.virtual_map[array_pos_new] == MONSTER_ROUTE:
            allow = True
            if self.virtual_map[array_pos_current] == entity.constant:
                self.virtual_map[array_pos_current] = GROUND
            self.virtual_map[array_pos_new] = entity.constant
            
        return allow
    
    def setBomb(self, bomb_position):
        bomb_array = matrixToArray(bomb_position[0],bomb_position[1])
        self.virtual_map[bomb_array] = BOMB
    
    
    def unsetBomb(self, bomb_position):
        
    
    
    def paint(self, screen, draw_grid=False):
        '''Desenha o cenário na tela'''
        self.map.paint(screen, draw_grid=True)
        
        for monster in self.monsters :
            monster.paint(screen)
