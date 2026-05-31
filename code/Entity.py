from abc import ABC, abstractmethod
import pygame
import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        try:
            self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        except:
            self.surf = pygame.Surface((1, 1), pygame.SRCALPHA)

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
