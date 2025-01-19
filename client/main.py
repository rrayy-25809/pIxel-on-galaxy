import pygame
import sys

# 게임 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def __init__(mainscreen):
    global screen , SCREEN_WIDTH , SCREEN_HEIGHT
    if not (mainscreen is None):
        screen = mainscreen

# 게임 초기화
pygame.init()
clock = pygame.time.Clock()