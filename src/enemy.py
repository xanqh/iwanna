import pygame
from game import *
from enemy_shot import Enemy_shot

class Enemy(pygame.sprite.Sprite):
    def __init__(self, shot_group, SE, target):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = screen_width // 2
        self.rect.bottom = screen_height + 7
        self.hp = 10
        self.damage = 1
        self.shot_group = shot_group
        self.attack_timer = 0
        self.SE = SE
        self.target = target
        # self.kid_x = kid.rect.x
        # self.kid_y = kid.rect.y

    def isAlive(self):
        if self.hp <= 0:
            self.kill()
            print("win!")

    def attack(self):
        self.attack_timer += 1
        if self.attack_timer > 50:
            target_x = self.target.rect.centerx
            target_y = self.target.rect.centery
            Enemy_shot(self.rect.x, self.rect.y, self.SE, target_x, target_y)
            print("OK")
            self.attack_timer = 0


    def update(self):
        self.attack()
        for shot in self.shot_group:
            if self.rect.colliderect(shot.rect):
                self.hp -= self.damage
                shot.kill()
                self.isAlive()
