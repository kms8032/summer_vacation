import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

# 배경
screen.fill((255,255,255))

# 원그리기(갯수)
circle = random.randint(5,20)

for circle_draw in range(circle):
    # 색
    colorR = random.randint(0,255)
    colorG = random.randint(0,255)
    colorB = random.randint(0,255)
    # 위치
    x = random.randint(101,699)
    y = random.randint(101,499)
    # 반지름
    r = random.randint(0,100)
    # 그리기
    pygame.draw.circle(screen,(colorR,colorG,colorB),(x,y),r)

# 화면 업데이트
pygame.display.flip()

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()