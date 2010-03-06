import pygame
MAPS = dict()
MAPS['Map01'] = {'background':'imagem/map/map01/background01.jpeg','sprites':('imagem/map/map01/mapa01.jpeg',1),
'map':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}

MAPS['Map02'] = {'background':'imagem/map/map02/background02.jpeg','sprites':('imagem/map/map02/mapa02.jpeg',2),
'map':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,2,0,0,2,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,2,0,0,2,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,2,0,0,2,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,2,0,0,2,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}

class Map :
    '''Define o mapa carregado na fase'''
    def __init__(self,map_name):
        '''Construtor da classe Map'''
        self.__background = MAPS[map_name]['background']
        self.__sprites = MAPS[map_name]['sprites']
        self.__map = MAPS[map_name]['map']
        self.background = self.__loadBackground__()
        self.sprites = self.__loadSprites__()

    def __loadBackground__(self) :
        '''Carrega a imagem de fundo do mapa e a retorna'''
        return pygame.image.load(self.__background).convert()
        

    def __loadSprites__(self) :
        '''Carrega cada uma das imagens do mapa e retorna uma lista com essas imagens'''
        sprites_image_filename = self.__sprites[0]
        sprites_image_quantity = self.__sprites[1]
        
        sprites_image = pygame.image.load(sprites_image_filename).convert_alpha()
        sprites = list()
        for i in range(0,sprites_image_quantity) :
            sprites.append(sprites_image.subsurface(pygame.Rect(i*32,0,32,32)))
        return sprites
        
    def paint(self,screen) :
        '''Exibe na tela as imagens do mapa'''
        screen.blit(self.background,(0,0))
        i = 0
        while i < len(self.__map) :
            s = self.__map[i]
            linha = i / 16
            coluna = i % 16
            if s > 0 :
                screen.blit(self.sprites[s-1],(linha*32,coluna*32))
            i += 1