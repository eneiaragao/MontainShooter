#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf=pygame.image.load('./asset/MenuBg.png')
        self.rect=self.surf.get_rect(left=0, top=0)

    def run(self, ):#funcção para colocar texto na tela do jogo e formatação
        menu_option=0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:  #draw imagens  (desenhando as imagens)
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 60))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):#evento para colocar a cor na tela onde esta o cursor
                if i==menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 180+25*i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 25 * i))

            pygame.display.flip()


           # Check for all events   (checando os eventos)
            for event in pygame.event.get():#evento para fechar a tela do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # END PYGAME
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:# verifica se o evento para percorrer as opções da tela para baixo
                        if menu_option <len (MENU_OPTION)-1:
                            menu_option+=1
                        else:
                            menu_option=0

                    if event.key == pygame.K_UP:# verifica se evento para percorrer as opções da tela cima
                        if menu_option >0:
                            menu_option-=1
                        else:
                            menu_option=len(MENU_OPTION)-1

                    if event.key == pygame.K_RETURN:  # verifica se evento para TECLA ENTER
                        return MENU_OPTION[menu_option]





# tela do jogo
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
