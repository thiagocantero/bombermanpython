import pygame
from pygame.locals import *
from pygame import Rect
from sys import exit

DIRECAO_CIMA = 1
DIRECAO_BAIXO = 2
DIRECAO_DIREITA = 3
DIRECAO_ESQUERDA = 4

SPRITE_VELX = SPRITE_VELY = 4

SPRITE_POS_CIMA = 0
SPRITE_POS_BAIXO = 192
SPRITE_POS_ESQUERDA = 288
SPRITE_POS_DIREITA = 96

SPRITE_TAM = (32,32)

sprite_passo = 0
sprite_pos = SPRITE_POS_CIMA

def desenhaGrade(surface) :
    for i in range(0, 16) :
        pygame.draw.line(surface, pygame.Color(0, 0, 0, 0), (i*32, 0), (i*32, 16*32), 1)
        
    for i in range(0, 16) :
        pygame.draw.line(surface, pygame.Color(0, 0, 0, 0), (0, i*32), (16*32, i*32), 1)        
    

pygame.init()
pygame.key.set_repeat(True)

background_image_filename = 'imagem/map/map01/background01.jpeg'
char_image_filename = 'imagem/bomberman.png'

screen = pygame.display.set_mode((512,512), 0, 32)
pygame.display.set_caption('Bomberman')

background_image = pygame.image.load(background_image_filename).convert()
char_image = pygame.image.load(char_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_rect = Rect(32,0,32,32)

char_direction = DIRECAO_CIMA
char_moving = False
x = y = 0

while True :

    for event in pygame.event.get() :
        if event.type == QUIT :
            exit(0)
        elif event.type == KEYDOWN :
            if not char_moving :
                if event.key == K_UP :
                    char_direction = DIRECAO_CIMA
                    char_moving = True
                elif event.key == K_DOWN :
                    char_direction = DIRECAO_BAIXO
                    char_moving = True
                elif event.key == K_LEFT :
                    char_direction = DIRECAO_ESQUERDA
                    char_moving = True
                elif event.key == K_RIGHT :
                    char_direction = DIRECAO_DIREITA
                    char_moving = True

    time_passed = clock.tick(12)
      
        

    if char_moving :
        if char_direction == DIRECAO_CIMA :
            y -= SPRITE_VELY
            sprite_pos = SPRITE_POS_CIMA
            sprite_rect = Rect((sprite_passo*32+sprite_pos,0),SPRITE_TAM)
            sprite_passo += 1
            sprite_passo %= 3
            if y%32 == 0 :
                char_moving = False
        elif char_direction == DIRECAO_BAIXO :
            y += SPRITE_VELY
            sprite_pos = SPRITE_POS_BAIXO
            sprite_rect = Rect((sprite_passo*32+sprite_pos,0),SPRITE_TAM)
            sprite_passo += 1
            sprite_passo %= 3
            if y%32 == 0 :
                char_moving = False
                            
        elif char_direction == DIRECAO_ESQUERDA :
            x -= SPRITE_VELX
            sprite_pos = SPRITE_POS_ESQUERDA
            sprite_rect = Rect((sprite_passo*32+sprite_pos,0),SPRITE_TAM)
            sprite_passo += 1
            sprite_passo %= 3
            if x%32 == 0 :
                char_moving = False
        elif char_direction == DIRECAO_DIREITA :
            x += SPRITE_VELX
            sprite_pos = SPRITE_POS_DIREITA
            sprite_rect = Rect((sprite_passo*32+sprite_pos,0),SPRITE_TAM)
            sprite_passo += 1
            sprite_passo %= 3
            if x%32 == 0 :
                char_moving = False
    else:
        sprite_rect = Rect((sprite_pos,0),SPRITE_TAM)
      
      
      
    if x < 0 :
        x = 0
        char_moving = False
    if x > 512-32 :
        x = 512-32
        char_moving = False
    if y < 0 :
        y = 0
        char_moving = False
    if y > 512-32 :
        y = 512-32
        char_moving = False
        
            

    
    sprite = char_image.subsurface(sprite_rect)
    
    screen.blit(background_image,(0,0))
    desenhaGrade(screen)
    screen.blit(sprite,(x,y))

    time_passed = clock.tick(30)

    pygame.display.update()

