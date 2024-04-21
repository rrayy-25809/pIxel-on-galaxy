import pygame
import random

class Meteor:
    def __init__(self, screen_width):
        # 문제: 이미지를 로드하고 크기를 조정해야 하지만, 현재 코드에서는 두 번 크기를 변경하고 있습니다.
        meteor_image = pygame.image.load("client/meteor.png")
        self.image = pygame.transform.scale(meteor_image, (115, 145))
        # 수정: 이미지 크기를 조정할 때 이미지의 너비와 높이를 사용해야 합니다.
        # self.image = pygame.transform.scale(meteor_image, (30, 30))
        
        # 문제: Rect를 생성하고 즉시 다른 Rect로 대체합니다.
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(random.randint(0, screen_width - 30), 0, 30, 30)
        # 수정: 생성된 Rect를 사용하고 위치와 크기를 설정합니다.
        # self.rect = pygame.Rect(random.randint(0, screen_width - 30), 0, 30, 30)

    def move(self):
        self.rect.y += 5

    def draw(self, screen):
        # 문제: draw 메서드는 이미지를 그리려고 시도하지만, Rect를 사용해야 합니다.
        # pygame.draw.rect(screen, self.rect)  # 잘못된 방법
        screen.blit(self.image, self.rect)  # 수정: 이미지를 화면에 그립니다.
