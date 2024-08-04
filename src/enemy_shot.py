import pygame
import math

class Enemy_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, SE, target_x, target_y):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/shot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.SE = SE
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 1

        # derection
        self.dx = self.target_x - x
        self.dy = self.target_y - y
        distance = math.hypot(self.dx, self.dy)
        self.dx = self.dx / distance * self.speed
        self.dy = self.dy / distance * self.speed

    def shot_sound(self):
        self.SE.play()


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
