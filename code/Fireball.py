import pygame
from code.Entity import Entity

class Fireball(Entity):
    def __init__(self, position):
        super().__init__('', position)
        self.name = 'Fireball'
        self.frames = []
        for i in range(1, 7):
            img = pygame.image.load(
                f'./asset/Boss.fire{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (80, 80)
            )
            img = pygame.transform.flip(
                img,
                True,
                False
            )
            self.frames.append(img)
        self.animation_counter = 0
        self.animation_speed = 0.25
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(
            center=position
        )
        self.speed = 6
        self.damage = 5
        self.health = 1

    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= len(self.frames):
            self.animation_counter = 0
        frame = int(self.animation_counter)
        self.surf = self.frames[frame]

    def move(self):
        self.animate()
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.health = 0