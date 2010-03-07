import pygame
import random
from constants import *
from map import Map

class Scenario :
    '''Define o cenário da fase. Cenário inclui: mapa, itens, caixas destrutíveis e saída'''
    def __init__(self, map_name) :
        '''Construtor da classe Scenario'''
        self.map = Map(map_name)
        self.virtual_map = __createVirtualMap__()
        self.items = None
        self.exit = None
        self.monsters = self.__createMonsters__()
        
    def __createVirtualMap__(self) :
        self.virtual_map = self.map.getMap()
        
    def __createMonsters__(self, quantity=3) :
        '''Cria quantity monstros em posições aleatórias'''
        pass
            
            
        
    def paint(self, screen, draw_grid=False):
        '''Desenha o cenário na tela'''
        self.map.paint(screen, draw_grid=True)
        
        for monster in self.monsters :
            #monster.move()
            monster.paint()
