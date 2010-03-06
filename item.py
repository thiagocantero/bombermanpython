import pygame
from constants import *

class Item :
    '''Define um item'''
    def __init__(self, file_name, time_duration, screen_position) :
        '''Construtor da classe Item
        - file_name: nome do arquivo do item
        - time_duration: tempo de duração do item (em ms) do efeito do item no bomberman
        '''
        self.__file_name = file_name
        self.__sprite = self.__loadSprite__()
        self.__time_start = None
        self.__time_duration = time_duration
        self.__position = screen_position
        self.bomberman = None
        
    def __loadSprite__(self) :
        '''Carrega o sprite do item'''      
        return pygame.image.load(self.__file_name).convert_alpha()
        
    def __isUsing__():
        '''Verifica se o item está sendo usado'''
        return self.__time_start == None
        
    def __setEffect__(self) :
        '''Aplica o efeito do item no bomberman'''
        pass
        
    def __unsetEffect__(self) :
        '''Remove o efeito do item do bomberman'''
        pass       
        
    def startUsing(self, time) :
        '''Inicia o item no bomberman'''
        self.__time_start = None #getTime(), por exemplo
        self.__setEffect__(self)
        
    def paint(self, screen):
        '''Desenha o item na tela'''
        if not self.__isUsing__() :
            screen.blit(sprite,self.__position)
        
        
        
class ItemVelocidade(Item) :
    '''Define um item que aumenta a velocidade do Bomberman por um certo tempo'''
    boost = 2
    def __init__(self,position) :
        '''Construtor da classe ItemVelocidade'''
        Item.__init__(self,'imagem/items/itemVelocidade.png', 2000, position)
        
    def __setEffect__(self) :
        '''Aplica o efeito do item no bomberman'''
        self.bomberman.velocity += ItemVelocidade.boost
        
    def __unsetEffect__(self) :
        '''Remove o efeito do item do bomberman'''
        self.bomberman.velocity -= ItemVelocidade.boost
        
    def tryFinish(self, time) :
        '''Verifica se o tempo de duração do item terminou e remove o efeito do item do bomberman, retornando True se o tempo de duração terminou e False, caso contrário'''
        if (time - self.__time_start) >= self.__time_duration :
            self.__unsetEffect__(self)
            return True
        return False