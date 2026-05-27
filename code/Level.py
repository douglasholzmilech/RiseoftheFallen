#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        pygame.mixer_music.load('./asset/mapa1.wav')
        pygame.mixer_music.play(-1)
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest= ent.rect)
                ent.move()
            pygame.display.flip()
        pass
