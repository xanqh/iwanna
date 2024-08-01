import pygame
from setting import *
from shot import Shot

class Kid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/kid.png").convert()
        self.speed = 3
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 4
        self.rect.y = 0
        self.fire = False
        self.timer = 0

    def isFire(self):
        global timer
        self.timer += 1
        if self.timer > 20:
            self.fire = False
            self.timer = 0

    def update(self):
        self.isFire()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if pressed_keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if pressed_keys[pygame.K_z] and self.fire == False:
            Shot(self.rect.x, self.rect.y)
            self.fire = True
