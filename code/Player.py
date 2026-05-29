#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        self.speed = 3
        self.defending = False

        self.dead_frames = []

        for i in range(1, 7):
            img = pygame.image.load(
                f'./asset/P1dead{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (100, 100))

            self.dead_frames.append(img)

        self.dead = False
        self.dead_animation_finished = False
        self.dead_counter = 0
        self.dead_speed = 0.15

        # VIDA
        self.max_health = 100
        self.health = 100

        # DIREÇÃO
        self.facing_right = True

        # =========================
        # WALK
        # =========================
        self.walk_frames = []

        for i in range(1, 9):
            img = pygame.image.load(
                f'./asset/P1walk{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (64, 64))

            self.walk_frames.append(img)

        # =========================
        # ATTACK 1
        # =========================
        self.attack1_frames = []

        for i in range(1, 5):
            img = pygame.image.load(
                f'./asset/P1attack1.{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (64, 64))

            self.attack1_frames.append(img)

        # =========================
        # ATTACK 2
        # =========================
        self.attack2_frames = []

        for i in range(1, 5):
            img = pygame.image.load(
                f'./asset/P1attack2.{i}.png'
            ).convert_alpha()

            img = pygame.transform.scale(img, (70, 70))

            self.attack2_frames.append(img)

        # =========================
        # DEFEND
        # =========================
        self.defend_frame = pygame.image.load(
            './asset/P1defend.png'
        ).convert_alpha()

        self.defend_frame = pygame.transform.scale(
            self.defend_frame,
            (64, 64)
        )

        # =========================
        # ANIMAÇÃO
        # =========================
        self.current_frame = 0
        self.animation_speed = 0.2
        self.animation_counter = 0

        self.state = 'idle'

        self.surf = self.walk_frames[0]

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

        # COMBATE
        self.attack = False
        self.attack_damage = 10
        self.attack_type = 0
        self.attack_cooldown = 0

    # =====================================
    # ANIMAÇÃO
    # =====================================

    def animate(self, frames):

        self.animation_counter += self.animation_speed

        # terminou animação
        if self.animation_counter >= len(frames):

            self.animation_counter = 0
            self.current_frame = 0

            # terminou ataque
            if self.state in ['attack1', 'attack2']:
                self.state = 'idle'
                self.attack = False

            return

        self.current_frame = int(self.animation_counter)

        image = frames[self.current_frame]

        # vira personagem
        if not self.facing_right:
            image = pygame.transform.flip(image, True, False)

        self.surf = image

    # =====================================
    # HITBOX ATAQUE
    # =====================================

    def get_attack_rect(self):

        if self.facing_right:
            return pygame.Rect(
                self.rect.right,
                self.rect.top + 10,
                5,
                self.rect.height - 20
            )

        else:
            return pygame.Rect(
                self.rect.left - 5,
                self.rect.top + 10,
                5,
                self.rect.height - 20
            )

    # =====================================
    # MOVIMENTO
    # =====================================

    def move(self):
        if self.dead:
            self.animate_death()
            return

        pressed_key = pygame.key.get_pressed()

        moving = False

        # cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # =====================================
        # =====================================
        # DEFESA
        # =====================================

        if pressed_key[pygame.K_KP0]:

            self.defending = True
            self.state = 'defend'

            image = self.defend_frame

            if not self.facing_right:
                image = pygame.transform.flip(image, True, False)

            self.surf = image

            return

        else:
            self.defending = False

        # =====================================
        # =====================================
        # ATTACK 1
        # =====================================

        if pressed_key[pygame.K_KP1] and self.attack_cooldown == 0:

            self.state = 'attack1'
            self.attack = True
            self.attack_type = 1
            self.attack_cooldown = 40

            self.animation_counter = 0
            self.current_frame = 0

        # =====================================
        # ATTACK 2
        # =====================================

        elif pressed_key[pygame.K_KP2] and self.attack_cooldown == 0:

            self.state = 'attack2'
            self.attack = True
            self.attack_type = 2
            self.attack_cooldown = 40

            self.animation_counter = 0
            self.current_frame = 0

        # =====================================
        # EXECUTA ATAQUE
        # =====================================

        if self.state == 'attack1':
            self.animate(self.attack1_frames)
            return

        if self.state == 'attack2':
            self.animate(self.attack2_frames)
            return

        # =====================================
        # MOVIMENTO
        # =====================================

        if pressed_key[pygame.K_UP] and self.rect.top > 250:
            self.rect.centery -= self.speed
            moving = True

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
            moving = True

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.speed
            self.facing_right = False
            moving = True

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed
            self.facing_right = True
            moving = True

        # =====================================
        # WALK
        # =====================================

        if moving:
            self.state = 'walk'
            self.animate(self.walk_frames)

        else:
            self.state = 'idle'

            image = self.walk_frames[0]

            if not self.facing_right:
                image = pygame.transform.flip(image, True, False)

            self.surf = image
    # =====================================
    # BARRA DE VIDA
    # =====================================

    def draw_health_bar(self, window):

        # fundo vermelho
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (20, 20, 200, 20)
        )

        # vida atual
        current_width = (
            self.health / self.max_health
        ) * 200

        pygame.draw.rect(
            window,
            (0, 255, 0),
            (20, 20, current_width, 20)
        )

        # borda branca
        pygame.draw.rect(
            window,
            (255, 255, 255),
            (20, 20, 200, 20),
            2
        )

    def animate_death(self):

        if self.dead_animation_finished:
            return

        self.dead_counter += self.dead_speed

        frame = int(self.dead_counter)

        if frame >= len(self.dead_frames):
            frame = len(self.dead_frames) - 1
            self.dead_animation_finished = True

        self.surf = self.dead_frames[frame]