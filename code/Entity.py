#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame
import pygame.image

from Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name

        # carrega imagem
        self.surf = pygame.image.load('./asset/' + name + '.png')

        # redimensiona
        self.surf = pygame.transform.scale(
            self.surf,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

        self.speed = 0

    @abstractmethod
    def move(self):
        pass