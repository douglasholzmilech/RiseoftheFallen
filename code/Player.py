#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name , position  ):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (64, 64))

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 250:
            self.rect.centery -= 1
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 1
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 1
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 1