import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
black = (0,0,0)
screen.fill(black)


running = True
while running :
    # 색
    colorRGB = random.sample(range(255),3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 사용자가 윈도우 닫기 버튼을 클릭하면 발생하는 이벤트
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, colorRGB, (event.pos),50)
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill(black)
            pygame.display.flip()
            
pygame.quit()