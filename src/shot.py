import pygame
from game import *
from setting import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, SE, direction):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/shot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.x = x
        self.rect.y = y
        self.SE = SE
        self.direction = direction

    def shot_sound(self):
            self.SE.play()


    def update(self):
        if self.direction == RIGHT:
            self.rect.x += self.speed
        else:
             self.rect.x -= self.speed
        if not -1 < self.rect.x < screen_width or not -1 < self.rect.y < screen_height:
            self.kill()
