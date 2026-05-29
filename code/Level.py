#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Database import Database

from Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 60000
        self.window = window
        self.name = name
        self.score = 0
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
            player = None

            for ent in self.entity_list:
                if ent.name == 'Player':
                    player = ent
                    break

            for ent in self.entity_list:

                self.window.blit(source=ent.surf, dest=ent.rect)

                if ent.name in ('Lizard', 'Medusa', 'Demon'):
                    ent.move(player)
                else:
                    ent.move()

            for ent in self.entity_list:

                if ent.name in ('Lizard', 'Medusa', 'Demon'):

                    if ent.attack_finished:

                        ent.attack_finished = False

                        if ent.rect.colliderect(player.rect):

                            if not player.defending:
                                player.health -= ent.damage

            player = None

            for entity in self.entity_list:
                if entity.name == 'Player':
                    player = entity
                    break

            # player atacando
            if player and player.attack:

                attack_rect = player.get_attack_rect()

                for entity in self.entity_list:

                    for entity in self.entity_list:

                        # somente entidades com vida
                        if hasattr(entity, 'health'):

                            # evita bater no player
                            if entity.name != 'Player':

                                # colisão
                                if attack_rect.colliderect(entity.rect):

                                    # ATTACK 1
                                    if player.attack_type == 1:
                                        damage = 10

                                    # ATTACK 2
                                    elif player.attack_type == 2:
                                        damage = 20

                                    else:
                                        damage = 0

                                    entity.health -= damage

            # REMOVE INIMIGOS MORTOS
            new_entity_list = []

            for ent in self.entity_list:

                # mantém player
                if ent.name == 'Player':
                    new_entity_list.append(ent)

                # mantém backgrounds
                elif 'Level1bg' in ent.name:
                    new_entity_list.append(ent)

                # mantém inimigos vivos
                elif hasattr(ent, 'health'):

                    if ent.health > 0:

                        new_entity_list.append(ent)

                    else:

                        if ent.name == 'Lizard':
                            self.score += 10

                        elif ent.name == 'Medusa':
                            self.score += 20

                        elif ent.name == 'Demon':
                            self.score += 30

            self.entity_list = new_entity_list


            # DESENHA BARRA DE VIDA DO PLAYER
            for ent in self.entity_list:
                if ent.name == 'Player':
                    ent.draw_health_bar(self.window)

            for ent in self.entity_list:

                if ent.name == 'Player' and ent.health <= 0:

                    ent.dead = True

                    while not ent.dead_animation_finished:

                        clock.tick(60)

                        self.window.fill((0, 0, 0))

                        for obj in self.entity_list:

                            if obj.name == 'Player':
                                obj.animate_death()

                            self.window.blit(obj.surf, obj.rect)

                        pygame.display.flip()

                    font = pygame.font.SysFont("Arial", 80, bold=True)

                    text = font.render("GAME OVER", True, (255, 0, 0))

                    rect = text.get_rect(center=(400, 300))

                    self.window.blit(text, rect)

                    pygame.display.flip()

                    pygame.time.delay(3000)
                    conn = Database.connect()

                    cursor = conn.cursor()

                    cursor.execute(
                        "INSERT INTO score(points) VALUES(?)",
                        (self.score,)
                    )

                    conn.commit()
                    conn.close()
                    return

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
            pygame.draw.rect(
                self.window,
                (0, 0, 0),
                (640, 15, 160, 30)
            )

            self.level_text(
                20,
                f'Score: {self.score}',
                COLOR_WHITE,
                (650, 20)
            )

            self.level_text(
                14,
                f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                COLOR_WHITE,
                (10, 5)
            )

            self.level_text(
                14,
                f'fps: {clock.get_fps():.0f}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 35)
            )
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)