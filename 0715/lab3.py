import pygame

pygame.init()

# 640x480
screen = pygame.display.set_mode((640,480))

running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 키보드의 키를 누르면 발생하는 이벤트
            # 눌린 키의 이름을 출력
            print(f"Key pressed: {pygame.key.name(event.key)}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} clicked at postion {event.pos}")
            
pygame.quit()