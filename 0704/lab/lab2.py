# 사용자로부터 행과 열을 수를 입력받아, 해당 크기에 맞는 2차원 리스트를 생성
# 사용자는 각 요소에 들어갈 값을 직접 입력
# 입력이 완료되면 완성된 2차원 리스트를 출력

# 절차
# 행과 열의 수를 입력
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
# 2차원 리스트 생성
two_dimensional_list = [[0 for _ in range(col)] for _ in range(row)]
# 리스트값 입력
for row_index in range(row):
    for col_index in range(col):
        two_dimensional_list[row_index][col_index] = int(input(f"Enter value for [{row_index}][{col_index}]: "))
# 출력
for i in two_dimensional_list:
    for j in i :
        print(j,end=" ")
    print()