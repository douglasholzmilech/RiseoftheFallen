import pygame
from code.Entity import Entity
from code.Fireball import Fireball


class Boss(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.damage = 20
        self.attack_finished = False
        self.max_health = 500
        self.health = 500
        self.walk_frames = []
        self.attack_frames = []
        self.death_frames = []
        self.fire_frames = []
        self.spawn_fireball = False
        for i in range(1, 7):
            img = pygame.image.load(
                f'./asset/Boss.fire{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (120, 120)
            )
            img = pygame.transform.flip(
                img,
                True,
                False
            )
            self.fire_frames.append(img)
        for i in range(1, 6):
            img = pygame.image.load(
                f'./asset/Boss.death{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (250, 250)
            )
            img = pygame.transform.flip(
                img,
                True,
                False
            )
            self.death_frames.append(img)
        for i in range(1, 5):
            img = pygame.image.load(
                f'./asset/Boss.attack{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (250, 250)
            )
            img = pygame.transform.flip(
                img,
                True,
                False
            )
            self.attack_frames.append(img)
        for i in range(1, 6):
            img = pygame.image.load(
                f'./asset/Boss.walk{i}.png'
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (250, 250)
            )
            img = pygame.transform.flip(
                img,
                True,
                False
            )
            self.walk_frames.append(img)
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = 0.15
        self.surf = self.walk_frames[0]
        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )
        self.speed = 2
        self.attacking = False
        self.attack_counter = 0
        self.attack_speed = 0.15
        self.dead = False
        self.dead_counter = 0
        self.dead_speed = 0.15
        self.dead_animation_finished = False
        self.attack_timer = 180
        self.state = 'walk'

    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= len(self.walk_frames):
            self.animation_counter = 0
        frame = int(self.animation_counter)
        self.surf = self.walk_frames[frame]

    def animate_attack(self):
        self.attack_counter += self.attack_speed
        frame = int(self.attack_counter)
        if frame == 2 and not self.spawn_fireball:
            self.spawn_fireball = True
        if self.attack_counter >= len(self.attack_frames):
            self.attack_counter = 0
            self.attacking = False
            self.attack_finished = True
            self.state = 'walk'
            self.spawn_fireball = False
            return
        self.surf = self.attack_frames[frame]

    def move(self, player=None):
        if self.health <= 0:
            self.dead = True
        if self.dead:
            self.animate_death()
            return
        if player:
            if player.rect.centerx < self.rect.centerx:
                self.rect.centerx -= self.speed
            elif player.rect.centerx > self.rect.centerx:
                self.rect.centerx += self.speed
            if player.rect.centery < self.rect.centery:
                self.rect.centery -= self.speed
            elif player.rect.centery > self.rect.centery:
                self.rect.centery += self.speed
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.attacking = True
                self.state = 'attack'
                self.attack_counter = 0
                self.attack_timer = 180
        if self.attacking:
            self.animate_attack()
        else:
            self.animate()

    def animate_death(self):
        self.dead_counter += self.dead_speed
        frame = int(self.dead_counter)
        if frame >= len(self.death_frames):
            frame = len(self.death_frames) - 1
            self.dead_animation_finished = True
        self.surf = self.death_frames[frame]

    def draw_health_bar(self, window):
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (300, 20, 300, 20)
        )
        width = (
                        self.health /
                        self.max_health
                ) * 300
        pygame.draw.rect(
            window,
            (0, 255, 0),
            (300, 20, width, 20)
        )
        pygame.draw.rect(
            window,
            (255, 255, 255),
            (300, 20, 300, 20),
            2
        )
