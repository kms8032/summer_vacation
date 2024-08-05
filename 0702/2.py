import random


def print_bingo_board(arg_list, col_num = 3):
    for index in range(len(arg_list)):
        print(arg_list[index],"\t",end="")
        
        if (index+1)%col_num == 3:
            print()


# n 값 입력
n = 3
bingo_elemnet_num = n * n
# n X n 빙고 보드 작성, 1차원 배열, 1~36사이의 중복되지 않는 정수


bingo_board = [1,2,3, \
               4,5,6, \
               7,8,9]

print_bingo_board(bingo_board)
bingo_count = 0
# 빙고 숫자가 2 미만일 경우
while bingo_count < 2 :
    bingo_count = 0
    
    # 랜덤 넘버 생성 1~36
    rand_num = random.randint(1,36)
    # 빙고 보드 내 생성된 랜덤 값이 있을 경우 "*"로 변경
    for index in range(bingo_elemnet_num):
        
    # 빙고 보드 출력
    
    # 빙고 검사