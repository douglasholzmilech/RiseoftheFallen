#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
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