#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity

class Boss(Entity):
    def __init__(self, name, position):
        self.walk_frames = []
        self.attack_frames = []
        self.death_frames = []
        self.max_health = 1000
        self.attack_timer = 0

        for i in range(1, 6):
            img = pygame.image.load(
                f'./asset/Boss.walk{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (250, 250))

            img = pygame.transform.flip(img, True, False)

            self.walk_frames.append(img)

        for i in range(1, 5):
            img = pygame.image.load(
                f'./asset/Boss.attack{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (250, 250))

            img = pygame.transform.flip(img, True, False)

            self.attack_frames.append(img)

        for i in range(1, 6):
            img = pygame.image.load(
                f'./asset/Boss.death{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (250, 250))

            img = pygame.transform.flip(img, True, False)

            self.death_frames.append(img)

        def move(self, player=None):
            if self.rect.centerx > 600:
                self.rect.centerx -= 1
            self.attack_timer += 1

            if self.attack_timer > 180:
                self.attacking = True
                self.attack_timer = 0