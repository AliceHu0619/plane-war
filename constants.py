import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_READY = os.path.join(ASSETS_DIR, 'images/background.png')
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')

IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')

BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')

TEXT_SOCRE_COLOR = pygame.Color(255, 255, 0)
SCORE_SHOOT_SMALL = 10

PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rest,txt')
OUR_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/hero1.png'), os.path.join(ASSETS_DIR, 'images/hero2.png')]

OUR_DESTORY_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')]

BULLET_IMG = os.path.join(ASSETS_DIR, 'image/bullet1.png')
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sound/bullet.wav')

SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/enemy1.png')]
SMALL_ENEMY_DESTORY_IMG_LIST = [os.path.join(ASSETS_DIR,'image/enemy1_down1.png'),os.path.join(ASSETS_DIR,'image/enemy1_down2.png'),os.path.join(ASSETS_DIR,'image/enemy1_down3.png'),os.path.join(ASSETS_DIR,'image/enemy1_down4.png')]

SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'sound/enemy1_down.wav')

