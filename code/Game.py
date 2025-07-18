
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        pygame.mixer_music.load('./asset/MusicaMenu.mp3')
        pygame.mixer_music.play(-1)


        while True:
            menu = Menu(self.window)
            menu_return =  menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pass






