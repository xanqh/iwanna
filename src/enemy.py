import pygame
from game import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, shot_group):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/enemy.png").convert()
        self.rect = self.image.get_rect()
        self.rect.left = screen_width // 2
        self.rect.bottom = screen_height + 7
        self.hp = 10
        self.damage = 1
        self.shot_group = shot_group
    
    def isAlive(self):
        if self.hp <= 0:
            self.kill()
            print("win!")

    def update(self):
        for shot in self.shot_group:
            if self.rect.colliderect(shot.rect):
                self.hp -= self.damage
                shot.kill()
                self.isAlive()
