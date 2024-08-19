import pygame
import random
# 초기화
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("도으라미 이동 및 색상 변경 프로그램")

# 색상 정의
colors = [(255,0,0),(0,0,0),(255,255,0),(0,255,0)(0,0,255)] # 빨 검 노 초 파
current_color = random.choice(colors)
circle_radius = 40


clock = pygame.time.Clock()
running = True

# 이벤트처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)
    
# 종료
pygame.quit()
