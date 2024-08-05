'''
# Two-dimensional_list
# 2차원 리스트

bar = [[1,2,3],[4,5,6],[7,8,9]]

# 6을 출력
print(bar[1][2])
'''

'''
# 생성 및 초기화
# 1. 직접 선언
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# or
matrix = [[0]*3]*5      # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(matrix)

# 2. list Comprehension
rows = 3
cols = 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]      # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(matrix)

# 3. List Comprehension (2)
# 3 x 4 행령 생성, 모든 값은 0
matrix = [[[0]*4] for _ in range(3)]     # [[[0, 0, 0, 0]], [[0, 0, 0, 0]], [[0, 0, 0, 0]]]
print(matrix)
'''

"""
# 데이터 접근 및 수정
# 3 x 2 Matrix 'bar' 생성
bar = [[10,20],[30,40],[50,60]]

# "bar" 리스트의 세 번째 행(인덱스 2)의 두 번째 열(인덱스 1)의 값을 출력
print(bar[2][1])

# "bar" 리스트의 첫 번쨰 행(인덱스 0)의 두 번쨰 열(인덱스 1)의 값을 100으로 변경
bar[0][1] = 100

# 변경된 "bar" 리스트의 첫 번째 행의 두 번째 열의 값을 출력
print(bar[0][1])
"""

# 데이터 순회
bar = [[10,20,30],[40,50],[60,70,80,90]]

# 'bar' Matrix의 모든 원소를 순회
for row in bar :
    for item in row :
        print(item,end=" ")
    print()