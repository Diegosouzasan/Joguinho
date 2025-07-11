#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_BLUE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/FundoMenu3.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/MusicaMenu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #DRAW IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Guardião da Chapada", COLOR_WHITE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 220 + 33 * i))
                    
                    

                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_BLUE, ((WIN_WIDTH / 2), 200 + 33 * i))

            self.menu_narrative_text(
                20,
                "As chamas tomaram a floresta, e homens de fogo surgiram das cinzas para destruir tudo.",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 310)
            )
            self.menu_narrative_text(
                20,
                "Você é a última esperança: assuma o controle da Onça Pintada, guardiã da natureza,",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 330)
            )
            self.menu_narrative_text(
                20,
                "e lute contra a destruição que assola a Chapada Diamantina.",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 350)
            )

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            if menu_option > 0:
                                menu_option -= 1

                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION [menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_narrative_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



