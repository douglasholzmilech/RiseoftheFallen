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
                    if i == 0:
                        list_level1.append(
                            Background(f'Level1bg{i}', (0, 0), speed=1)
                        )
                    else:
                        list_level1.append(
                            Background(f'Level1bg{i}', (0, 0), speed=0)
                        )

                return list_level1
            case 'Player':
                return Player('Player', (WIN_WIDTH / 2, 400))
            case 'Lizard':
                return Enemy('Lizard', (WIN_WIDTH + 10, random.randint(250, 500)))
            case 'Medusa':
                return Enemy('Medusa', (WIN_WIDTH + 10, random.randint(250, 500)))
            case 'Demon':
                return Enemy('Demon', (WIN_WIDTH + 10, random.randint(250, 500)))
            case 'Level2bg':
                list_level2 = []
                for i in range(7):
                    if i == 0:
                        list_level2.append(
                            Background(f'Level2bg{i}', (0, 0), speed=1)
                        )
                    else:
                        list_level2.append(
                            Background(f'Level2bg{i}', (0, 0), speed=0)
                        )
                return list_level2
            case 'Level3bg':
                list_level3 = []
                for i in range(8):
                    if i == 0:
                        list_level3.append(
                            Background(f'Level3bg{i}', (0, 0), speed=1)
                        )
                    else:
                        list_level3.append(
                            Background(f'Level3bg{i}', (0, 0), speed=0)
                        )
                return list_level3
            case 'Level4bg':
                list_level4 = []
                for i in range(8):
                    if i == 0:
                        list_level4.append(
                            Background(f'Level4bg{i}', (0, 0), speed=1)
                        )
                    else:
                        list_level4.append(
                            Background(f'Level4bg{i}', (0, 0), speed=0)
                        )
                return list_level4
            case 'Boss':
                from code.Boss import Boss
                return Boss('Boss', (WIN_WIDTH + 200, 250))
