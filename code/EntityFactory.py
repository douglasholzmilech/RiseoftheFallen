#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Const import WIN_WIDTH, WIN_HEIGHT
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1bg':
                list_level1 = []

                for i in range(7):

                    # primeira imagem se move
                    if i == 0:
                        list_level1.append(
                            Background(f'Level1bg{i}', (0, 0), speed=1)
                        )

                    # restantes ficam paradas
                    else:
                        list_level1.append(
                            Background(f'Level1bg{i}', (0, 0), speed=0)
                        )

                return list_level1
            case 'Player' :
                return Player('Player', (WIN_WIDTH/2,400))
            case 'Lizard':
                return Enemy('Lizard', (WIN_WIDTH + 10, random.randint(250, 500)))
            case 'Medusa':
                return Enemy('Medusa', (WIN_WIDTH + 10, random.randint(250, 500)))
            case 'Demon':
                return Enemy('Demon', (WIN_WIDTH + 10, random.randint(250, 500)))
