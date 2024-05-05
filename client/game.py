import pygame
import sys
from player import Player
from meteor import Meteor

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
score = 0
life = 3

# 플레이어 객체 생성
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 165)

# 물체 객체 리스트 생성
objects = []

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_right()
    # 플레이어가 화면 아래로 벗어났을 경우
    if player.rect.x > SCREEN_WIDTH:
        player.rect.x = 1
    if player.rect.x < -1:
        player.rect.x = SCREEN_WIDTH-1

    if len(objects) < 5:
        if pygame.time.get_ticks() % 30 == 0:
            obj = Meteor(SCREEN_WIDTH)
            objects.append(obj)

    # 물체 떨어뜨리기
    for obj in objects:
        obj.move()

        # 물체가 화면 아래로 벗어났을 경우
        if obj.rect.y > SCREEN_HEIGHT:
            objects.remove(obj)
            score += 1
        # 충돌 체크
        if obj.rect.colliderect(player.rect):
            life -= 1
            objects.remove(obj)
            if life == 0:
                pygame.quit()
                sys.exit()

    # 화면 지우기
    screen.fill(BLACK)

    # 플레이어 그리기
    player.draw(screen)

    # 물체 그리기
    for obj in objects:
        obj.draw(screen)

    # 점수 표시
    font = pygame.font.SysFont("DungGeunMo.ttf", 36)
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(60)