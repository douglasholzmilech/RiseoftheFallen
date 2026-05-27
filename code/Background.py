#!/usr/bin/python
# -*- coding: utf-8 -*-

from Const import WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed=0):
        super().__init__(name, position)
        self.speed = speed

    def move(self):

        self.rect.centerx -= self.speed

        # quando sair totalmente da tela
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH