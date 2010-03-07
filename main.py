import pygame
from pygame import Rect
from pygame.locals import *
from sys import exit

from constants import *
from scenario import Scenario
from monster import Monster
from bomberman import Bomberman

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H), 0, 32)
    pygame.display.set_caption('Bomberman')

    clock = pygame.time.Clock()

    scenario = Scenario('Map01')
    bomberman = Bomberman()

    while True :

        for event in pygame.event.get() :
            if event.type == QUIT :
                exit(0)

        time_passed = clock.tick(FPS)
        
        scenario.process()
        scenario.paint(screen,draw_grid=False)

        bomberman.process()
        bomberman.paint(screen)
        
        pygame.display.update()
        
if __name__ == '__main__' :
    main()
