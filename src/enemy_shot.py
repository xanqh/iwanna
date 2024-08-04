import pygame
import math
from setting import *

class Enemy_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, SE, target):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/shot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.float_x = float(x)
        self.float_y = float(y)
        self.SE = SE
        self.speed = 5
        target_x, target_y = target.rect.center

        # derection
        # print(f'kid_x : {target_x}, kid_y : {target_y}') # デバッグ用
        # print(f'enemy_x : {x}, enemy_y : {y}') # デバッグ用
        dx = target_x - x
        dy = target_y - y
        # print(f'dx : {dx}, dy : {dy}') # デバッグ用
        distance = math.sqrt(dx ** 2 + dy ** 2)
        # print('\033[31m'+f'distance : {distance}' + '\033[0m') # デバッグ用
        self.dx = dx / distance * self.speed
        self.dy = dy / distance * self.speed
        # print('\033[32m' + f'self.dx : {self.dx}, self.dy : {self.dy}' + '\033[0m') # デバッグ用

    def shot_sound(self):
        self.SE.play()


    def update(self):
        self.float_x += self.dx
        self.float_y += self.dy
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        # print('\033[33m' + f'self.float_y : {self.float_y}' + '\033[0m')
        # print('\033[35m' + f'self.rect.y : {self.rect.y}' + '\033[0m')
        if not -1 < self.rect.x < screen_width or not -1 < self.rect.y < screen_height:
           self.kill()
