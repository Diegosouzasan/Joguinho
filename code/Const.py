import pygame
from pygame.examples.grid import WINDOW_WIDTH

#c
COLOR_WHITE =  (240, 251, 248, 98)
COLOR_BLUE = (231, 249, 251, 98)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)


#y
COLOR_YELLOW = (252, 230, 40, 99)

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P- COMPETITIVE',
               'SCORE',
               'EXIT')



#p
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

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
    'Player1Shot': 3,  # Player tiro
    'Enemy1':1, #Inimigo1
    'Enemy1Shot': 5,  # Inimigo1 tiro
    'Enemy2':1, #Inimigo2
    'Enemy2Shot': 2,  # Inimigo1 tiro

}
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2':0,
    'Level1bg3':0,
    'Level1bg4':0,
    'Level1bg5':0,
    'Level1bg6':0,
    'Level1bg7':0,
    'Player1':1,
    'Player1Shot':25,
    'Enemy1':1,
    'Enemy1Shot': 20,
    'Enemy2':1,
    'Enemy2Shot':15,

}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200,

}

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
    'Player1Shot':1,  # Player 1
    #'PlayerShot': 1,  # Player 1
    'Enemy1':70, #Inimigo1 50
    'Enemy2':80, #Inimigo2 60
    'Enemy1Shot': 1,  # Inimigo1 tiro
    'Enemy2Shot': 1,  # Inimigo1 tiro

}


#w
WIN_WIDTH = 634
WIN_HEIGHT = 422

#s

SPAWN_TIME = 4000