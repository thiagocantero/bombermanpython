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
                
                m = Monster('Monster01',(x*SPRITE_W, y*SPRITE_H))
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
                    self.virtual_map[pos_monster] = MONSTER
                    self.map.destroyBox(pos_monster)
                    for (x_route, y_route) in pos_route :
                        pos = matrixToArray(x_route,y_route)
                        self.virtual_map[pos] = MONSTER_ROUTE
                        self.map.destroyBox(pos)

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
    
    
    def paint(self, screen, draw_grid=False):
        '''Desenha o cenário na tela'''
        self.map.paint(screen, draw_grid=True)
        
        for monster in self.monsters :
            monster.paint(screen)
