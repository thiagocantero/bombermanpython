import pygame
from constants import *
from map import Map
from monster import Monster
from pygame import Rect
from pygame.locals import *
from sys import exit

def desenhaGrade(surface) :
    for i in range(0, 16) :
        pygame.draw.line(surface, pygame.Color(0, 0, 0, 0), (i*32, 0), (i*32, 16*32), 1)
        
    for i in range(0, 16) :
        pygame.draw.line(surface, pygame.Color(0, 0, 0, 0), (0, i*32), (16*32, i*32), 1)   

pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H), 0, 32)
pygame.display.set_caption('Bomberman')

clock = pygame.time.Clock()

mapa = Map('Map01')
monster = [Monster('Monster04',(192,192))]

while True :

    for event in pygame.event.get() :
        if event.type == QUIT :
            exit(0)

    time_passed = clock.tick(FPS)
    
    mapa.paint(screen)
    desenhaGrade(screen)
    for m in monster :
        m.move()
        m.paint(screen)
        
    pygame.display.update()

