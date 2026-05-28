#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        if name == 'Lizard':
            self.surf = pygame.transform.scale(self.surf, (200, 200))

        elif name == 'Medusa':
            self.surf = pygame.transform.scale(self.surf, (100, 100))

        elif name == 'Demon':
            self.surf = pygame.transform.scale(self.surf, (200, 200))

        self.surf = pygame.transform.flip(self.surf, True, False)

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
