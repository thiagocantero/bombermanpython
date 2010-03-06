import pygame

class Item :
    '''Define um item'''
    def __init__(self) :
        '''Construtor da classe Item'''
        self.__file_name = None
        self.sprite = None
        self.start = None
        self.duration = None
        self.position = None
        
    def paint(self, screen):
        '''Desenha o item na tela'''
        screen.blit(sprite,self.position)
