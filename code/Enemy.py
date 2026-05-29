#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

        # LISTA DE FRAMES
        self.frames = []

        # QUANTIDADE DE FRAMES
        frame_count = {
            'Demon': 6,
            'Lizard': 6,
            'Medusa': 4
        }

        # TAMANHO DOS INIMIGOS
        size = {
            'Demon': (100, 100),
            'Lizard': (100, 100),
            'Medusa': (100, 100)
        }

        # CARREGA FRAMES
        for i in range(1, frame_count[name] + 1):

            # nomes dos arquivos
            # Demon.walk1.png
            # Lizard.walk1.png
            # Medusa.walk1.png

            img = pygame.image.load(
                f'./asset/{name}.walk{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, size[name])

            # vira para esquerda
            img = pygame.transform.flip(img, True, False)

            self.frames.append(img)

        # frame inicial
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = 0.15

        self.surf = self.frames[self.current_frame]

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )
        # VIDA
        self.max_health = 30
        self.health = 30

    def animate(self):
        self.animation_counter += self.animation_speed

        if self.animation_counter >= len(self.frames):
            self.animation_counter = 0

        self.current_frame = int(self.animation_counter)

        self.surf = self.frames[self.current_frame]

    def move(self):
        # movimenta
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # anima
        self.animate()

        # reaparece
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH