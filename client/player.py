import pygame
import time

class Player:
    def __init__(self, x,y):
        # 문제: 이미지를 로드하고 크기를 조정해야 하지만, 현재 코드에서는 두 번 크기를 변경하고 있습니다.
        player_image = pygame.image.load("client/player.png")
        self.image = pygame.transform.scale(player_image, (int(player_image.get_height())*2+5, int(player_image.get_height())*2+5))
        
        # 문제: Rect를 생성하고 즉시 다른 Rect로 대체합니다.
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x,y, 30, 30)

    def move_left(self):
        self.rect.x -= 3

    def move_right(self):
        self.rect.x += 3

    def draw(self, screen):
        # 문제: draw 메서드는 이미지를 그리려고 시도하지만, Rect를 사용해야 합니다.
        # pygame.draw.rect(screen, self.rect)  # 잘못된 방법
        screen.blit(self.image, self.rect)  # 수정: 이미지를 화면에 그립니다.
