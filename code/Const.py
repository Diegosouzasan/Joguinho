import pygame
from pygame.examples.grid import WINDOW_WIDTH

#c
COLOR_WHITE =  (240, 251, 248, 98)
COLOR_BLUE = (231, 249, 251, 98)

#y
COLOR_YELLOW = (252, 230, 40, 99)

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P- COMPETITIVE',
               'SCORE',
               'EXIT')

#e
ENTITY_SPEED = {
    'Level1bg0': 0, #Fundo
    'Level1bg1': 0.6, #Montanha
    'Level1bg2':1.6, #Abusto
    'Level1bg3':2, #Arvore
    'Level1bg4':3, #Nuvem 1
    'Level1bg5':1.6, #Flor1
    'Level1bg6':1.6, #Flor2
    'Level1bg7':1.6,  #Nuvem 2
    'Player1':3, #Player 1
    'Enemy1':2, #Inimigo1
    'Enemy2':1, #Inimigo2
}
EVENT_ENEMY = pygame.USEREVENT + 1


ENTITY_HEALTH = {
    'Level1bg0': 999, #Fundo
    'Level1bg1': 999, #Montanha
    'Level1bg2':999, #Abusto
    'Level1bg3':999, #Arvore
    'Level1bg4':999, #Nuvem 1
    'Level1bg5':999, #Flor1
    'Level1bg6':999, #Flor2
    'Level1bg7':999,  #Nuvem 2
    'Player1':300, #Player 1
    'Enemy1':50, #Inimigo1
    'Enemy2':60, #Inimigo2
}


#w
WIN_WIDTH = 634
WIN_HEIGHT = 422

#s

SPAWN_TIME = 4000