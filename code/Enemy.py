import pygame
from Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.frames = []
        frame_count = {
            'Demon': 6,
            'Lizard': 6,
            'Medusa': 4
        }
        size = {
            'Demon': (100, 100),
            'Lizard': (100, 100),
            'Medusa': (100, 100)
        }
        for i in range(1, frame_count[name] + 1):
            img = pygame.image.load(
                f'./asset/{name}.walk{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(img, size[name])
            img = pygame.transform.flip(img, True, False)
            self.frames.append(img)
        self.attack_frames = []
        attack_count = {
            'Lizard': 5,
            'Medusa': 6,
            'Demon': 4
        }
        for i in range(1, attack_count[name] + 1):
            img = pygame.image.load(
                f'./asset/{name}.attack{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(img, size[name])
            img = pygame.transform.flip(img, True, False)
            self.attack_frames.append(img)
        self.attacking = False
        self.attack_counter = 0
        self.attack_speed = 0.20
        self.attack_finished = False
        self.damage = {
            'Lizard': 5,
            'Medusa': 8,
            'Demon': 10
        }[name]
        self.attack_range = 70
        self.attack_cooldown = 0
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = 0.15
        self.surf = self.frames[self.current_frame]
        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )
        self.max_health = 10
        self.health = 10

    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= len(self.frames):
            self.animation_counter = 0
        self.current_frame = int(self.animation_counter)
        self.surf = self.frames[self.current_frame]

    def move(self, player=None):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if player:
            distance = abs(player.rect.centerx - self.rect.centerx)
            if distance <= self.attack_range:
                self.attacking = True
            elif not self.attacking:
                direction = pygame.math.Vector2(
                    player.rect.centerx - self.rect.centerx,
                    player.rect.centery - self.rect.centery
                )
                if direction.length() > 0:
                    direction = direction.normalize()
                    self.rect.centerx += direction.x * ENTITY_SPEED[self.name]
                    self.rect.centery += direction.y * ENTITY_SPEED[self.name]
        if self.attacking:
            self.animate_attack()
        else:
            self.animate()
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

    def animate_attack(self):
        self.attack_counter += self.attack_speed
        if self.attack_counter >= len(self.attack_frames):
            self.attack_counter = 0
            self.attacking = False
            self.attack_finished = True
        frame = int(self.attack_counter)
        self.surf = self.attack_frames[frame]
