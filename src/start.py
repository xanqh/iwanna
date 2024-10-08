import pygame
from setting import *
from enemy import Enemy
from kid import Kid
from shot import Shot
from enemy_shot import Enemy_shot

class Start:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.msc_setting()
        self.create_group()
        self.containers_setting()
        # 自機
        self.kid = Kid(self.enemy_shot_group, self.shot_se)
        # 音
        self.music_stop = True
        # スタートテキスト
        self.font = pygame.font.SysFont("DIN Alternate", 70)
        self.cmy = (120,120,120)
        self.start_text = self.font.render("Press Right Shift\nto start the game!!", True, self.cmy, None)

    def create_group(self):
        self.shot_group = pygame.sprite.Group()
        self.enemy_shot_group = pygame.sprite.Group()
        self.group = pygame.sprite.RenderUpdates()

    def msc_setting(self):
        pygame.mixer.music.load("../msc/startbgm.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
        self.shot_se = pygame.mixer.Sound("../msc/shot.mp3")
        self.shot_se.set_volume(0.4)

    def containers_setting(self):
        Kid.containers = self.group
        Shot.containers = self.group,self.shot_group

    def run(self):
        # print(self.shot_group) # デバッグ用
        self.screen.blit(self.start_text, (screen_width // 2 - 280, screen_height / 2 - 80))
        self.group.draw(self.screen)
        self.group.update()
        self.shot_group.draw(self.screen)
        self.shot_group.update()
        pygame.display.flip()
        self.screen.fill((219, 255, 208))