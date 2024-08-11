import pygame
from setting import *
from shot import Shot

class Kid(pygame.sprite.Sprite):
    def __init__(self, enemy_shot_group, SE):
        super().__init__(self.containers)
        self.screen = pygame.display.get_surface()
        self.animation_list = []
        self.image = pygame.image.load("../img/kid.png").convert_alpha()
        # self.image.fill((255,255,255)) #デバッグ用
        self.speed = 3
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 4
        self.rect.bottom = screen_height
        self.fire = False
        self.timer = 0
        self.vel = 0 # y方向の速度
        self.acc = 1 # 重力加速度
        self.canJump = True
        self.canJump2 = False
        self.SE = SE
        self.enemy_shot_group = enemy_shot_group
        self.font = pygame.font.SysFont("Arial", 80)
        self.end_text = self.font.render("GAME OVER!!", True, (255, 255, 255))
        self.gameover_flg = False
        self.jump_count = 0
        self.max_jumps = 2
        self.jump_pressed = False
        self.direction = RIGHT

    def isFire(self):
        global timer
        self.timer += 1
        if self.timer > 20:
            self.fire = False
            self.timer = 0

    def jump(self):
        if self.jump_count < self.max_jumps:
            self.jump_count += 1
            self.vel = -15
            self.canJump = False

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
            self.jump_count = 0

    def screen_detection(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        # if self.rect.bottom > screen_height:
        #     self.rect.bottom = screen_height

    def input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            if self.direction == RIGHT:
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = LEFT
            self.rect.x -= self.speed
        elif pressed_keys[pygame.K_RIGHT]:
            if self.direction == LEFT:
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = RIGHT
            self.rect.x += self.speed
        if pressed_keys[pygame.K_LSHIFT]:
            if not self.jump_pressed:
                self.jump()
                self.jump_pressed = True
        else:
            self.jump_pressed = False

    def shot(self):
        Shot(self.rect.centerx, self.rect.y, self.SE, self.direction)
        self.SE.play()

    def update(self):
        if not self.gameover_flg:
            self.screen_detection()
            self.isFire()
            self.input()
            self.kid_update()
            for enemy_shot in self.enemy_shot_group:
                if self.rect.colliderect(enemy_shot.rect):
                    self.gameover_flg = True
                    self.kill()
