
import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 예제: 움직이는 공")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 공 설정
ball_pos = [400, 300]
ball_radius = 20
ball_speed = 5

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_speed
    if keys[pygame.K_UP]:
        ball_pos[1] -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_pos[1] += ball_speed

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    pygame.display.flip()

    # FPS 설정
    pygame.time.Clock().tick(60)

# 종료
pygame.quit()
sys.exit()
