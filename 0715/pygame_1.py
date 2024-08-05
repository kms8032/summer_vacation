import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
print(screen.get_width(),screen.get_height())

center_x = int(screen.get_width() / 2)
center_y = int(screen.get_height() /2 )

# 색 정의
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# 점그리기
pygame.draw.circle(screen, RED, (center_x, center_y), 40) # 중앙
pygame.draw.circle(screen, GREEN, (0,0), 40)
pygame.draw.circle(screen, BLUE, (799, 599), 40)
pygame.display.flip()

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()