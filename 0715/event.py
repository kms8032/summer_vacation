import pygame

# 초기화
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Evnet Listener and Handler Example")
running = True

while running :
    # 이벤트 큐에서 이벤트를 가져옴
    for event in pygame.event.get():
        # 이벤트 출력
        print(event)
        
# 종료
pygame.quit()