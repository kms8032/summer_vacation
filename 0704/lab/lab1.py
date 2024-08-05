# 사용자로부터 start,end,n의 세 값을 입력
# 이 값들을 사용하여 start와 end 사이에서 중복되지 않은 N개의 난수를 생성 후 1차원 리스트에 저장 후 출력하는 프로그램 작성

# 난수 생성 (start,end,n)
import random

# start 입력
while True :
    start = int(input("Start (0 이상의 정수): "))
    if start >= 0 :
        break
    else :
        print("0 이상의 정수를 입력하세요.")

# end 입력
while True :
    end = int(input("End (Start보다 큰 정수): "))
    if end <= start :
        print(f"Start({end})보다 커야 합니다.")
    else : 
        break
# start와 end 사이의 정수를 담을 리스트 생성
n_list = []
# start와 end사이의 수를 리스트에 저장
for n in range(start,end+1):
    n_list.append(n)

# 생성할 난수의 개수 입력
while True :
    N = int(input("N (생성할 난수의 개수) :"))
    if N <= len(n_list):
        print(random.sample(n_list,N))
        break
    else :
        print(f"N은 {start}부터 {end}사이의 정수여야 합니다.")