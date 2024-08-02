import pygame
from setting import *
from shot import Shot
from game import *

class Kid(pygame.sprite.Sprite):
    def __init__(self, SE):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/kid.png").convert()
        self.speed = 3
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 4
        self.rect.bottom = screen_height
        self.fire = False
        self.timer = 0
        self.vel = 0 # y方向の速度
        self.acc = 1 # 重力加速度
        self.canJump = True
        self.SE = SE
        self.shot_se = pygame.mixer.Sound("../msc/shot.mp3")

    def isFire(self):
        global timer
        self.timer += 1
        if self.timer > 20:
            self.fire = False
            self.timer = 0

    def jump(self):
        if self.canJump:
            self.canJump = False
            self.vel = -15

    def kid_update(self):
        if self.canJump:
            return

        # 更新
        self.vel += self.acc
        self.rect.y += self.vel

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel = 0
            self.canJump = True

    def input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if pressed_keys[pygame.K_SPACE]:
            self.jump()
        if pressed_keys[pygame.K_z] and self.fire == False:
            self.shot_se.play()
            shot = Shot(self.rect.x, self.rect.y, self.SE)
            self.fire = True

    def update(self):
        self.isFire()
        self.input()
        self.kid_update()
