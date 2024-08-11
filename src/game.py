import pygame
from setting import *
from enemy import Enemy
from kid import Kid
from shot import Shot
from enemy_shot import Enemy_shot

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.msc_setting()
        self.create_group()
        self.containers_setting()
        # 自機
        self.kid = Kid(self.enemy_shot_group, self.shot_se)
        # 敵
        self.enemy = Enemy(self.shot_group, self.shot_se, self.kid)
        # 音
        self.music_stop = True
        # win text
        self.font = pygame.font.SysFont("DIN Alternate", 70)
        self.cmy = (120,120,120)
        self.win_text = self.font.render("win!!", True, self.cmy, None, screen_width)

    def create_group(self):
        self.shot_group = pygame.sprite.Group()
        self.enemy_shot_group = pygame.sprite.Group()
        self.group = pygame.sprite.RenderUpdates()

    def msc_setting(self):
        pygame.mixer.music.load("../msc/bgm.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
        self.shot_se = pygame.mixer.Sound("../msc/shot.mp3")
        self.shot_se.set_volume(0.4)
        self.gameover_se = pygame.mixer.Sound("../msc/gameover.mp3")
        self.gameover_se.set_volume(0.4)

    def containers_setting(self):
        Enemy.containers = self.group
        Kid.containers = self.group
        Shot.containers = self.group,self.shot_group
        Enemy_shot.containers = self.group, self.enemy_shot_group

    def reset(self):
        self.enemy_shot_group.empty()
        self.group.empty()
        self.kid = Kid(self.enemy_shot_group, self.shot_se)
        self.enemy = Enemy(self.shot_group, self.shot_se, self.kid)
        self.gameover_se.stop()
        pygame.mixer.music.play(-1)
        self.kid.gameover_flg = False
        self.music_stop = True

    def run(self):
        # print(self.shot_group) # デバッグ用
        # print(self.enemy_shot_group) # デバッグ用
        if self.kid.gameover_flg:
            self.screen.blit(self.kid.end_text, (screen_width // 2 - 240, screen_height / 2 - 40))  # ゲームオーバー画面を表示
            if self.music_stop:
                pygame.mixer.music.stop()
                self.gameover_se.play()
                self.music_stop = False
        if not self.enemy.alive:
            self.screen.blit(self.win_text, (screen_width // 2 - 90, screen_height / 2 - 70))
        self.group.draw(self.screen)
        self.group.update()
        self.shot_group.draw(self.screen)
        self.shot_group.update()
        pygame.display.flip()
        self.screen.fill((0,0,0))