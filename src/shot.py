import pygame
from setting import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/shot.png")
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speed

        if not -1 < self.rect.x < screen_width or not -1 < self.rect.y < screen_height:
            self.kill()
