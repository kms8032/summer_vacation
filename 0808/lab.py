import pygame
import random

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_heigt = 800, 600
screen = pygame.display.set_mode((screen_width, screen_heigt))
pygame.display.set_caption("Collect Items Game")

# 색상 저으이
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)

# 장애물 생성 함수 (충돌되지 않는 장애물들 생성)
def create_obstacles(num_obstacles, size, screen_width, screen_height):
    # 주어진 수만큼 장애물을 생성하고, 서로 겹치지 않도록 설정
    obstacles = []
    for _ in range(num_obstacles):
        while True :
            rect = pygame.Rect(random.randint(0, screen_width - size), random.randint(0, screen_height - size) , size, size)
            if not any(rect.colliderect(o) for o in obstacles):     # 다른 장애물과 겹치지 않음
                obstacles.append(rect)
                break
    return obstacles
    
# 아이템 생성 함수
def create_items(num_items, size, screen_width, screen_height):
    # 주어진 수만큼 아이템 생성하고, 장애물 및 다름 아이템과 겹치지 않도록 위치를 설정
    items = []
    for _ in range(num_items):
        