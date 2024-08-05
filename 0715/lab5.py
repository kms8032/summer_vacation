import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
# 무작위 색상 생성
# 시작점(화면중앙)
x, y = ((400,300))

# 루프 설정
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            color = random.sample(range(255),3)
            if event.key == pygame.K_UP:
                pygame.draw.line(screen,color,(x,y),(x,y-10))
                y -= 10
            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen,color,(x,y),(x,y+10))
                y += 10
            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen,color,(x,y),(x+10,y))
                x += 10
            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen,color,(x,y),(x-10,y))
                x -= 10
        pygame.display.flip()
pygame.quit()