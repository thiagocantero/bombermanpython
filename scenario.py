import pygame
from map import Map

class Scenario :
    '''Define o cenário da fase. Cenário inclui: mapa, itens, caixas destrutíveis e saída'''
    def __init__(self, map_name) :
        '''Construtor da classe Scenario'''
        self.map = Map(map_name)
        self.items = None
        self.boxes = None
        self.exit = None
        
    def paint(self, screen, draw_grid=False):
        '''Desenha o cenário na tela'''
        self.map.paint(screen, draw_grid=True)
