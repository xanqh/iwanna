import pygame
from game import *
from enemy_shot import Enemy_shot
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, shot_group, SE, target):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/enemy.png").convert_alpha()
        self.image.fill((255,255,255)) #デバッグ用
        self.rect = self.image.get_rect()
        self.rect.right = screen_width - 10
        self.rect.bottom = screen_height + 7
        self.hp = 10
        self.damage = 1
        self.shot_group = shot_group
        self.attack_timer = 0
        self.SE = SE
        self.target = target
        self.dy = 0
        self.hit_se = pygame.mixer.Sound("../msc/hit.mp3")
        # self.kid_x = kid.rect.x
        # self.kid_y = kid.rect.y

    def isAlive(self):
        if self.hp <= 0:
            self.kill()
            print("win!")

    def attack(self):
        self.attack_timer += 1
        if self.attack_timer > 50:
            enemy_shot = Enemy_shot(self.rect.centerx, self.rect.centery, self.SE, self.target)
            # enemy_shot.shot_sound()
            self.attack_timer = 0

    def move(self):
        if self.rect.bottom > screen_height:
            self.dy = -3
        if self.rect.top < 0:
            self.dy = 3
        self.rect.centery += self.dy


    def update(self):
        # print(self.rect.centery)
        self.attack()
        self.move()
        for shot in self.shot_group:
            if self.rect.colliderect(shot.rect):
                self.hit_se.play()
                self.hp -= self.damage
                shot.kill()
                self.isAlive()
