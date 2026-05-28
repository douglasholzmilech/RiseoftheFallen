#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 60000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self, ):
        pygame.mixer_music.load('./asset/mapa1.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Lizard', 'Medusa', 'Demon'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
