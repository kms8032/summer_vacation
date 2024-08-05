# 직접 선언
# 2 X 3 X 3 
bar = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]

# list comprehension
# 2 X 3 X 4
# bar = [[[0 for col in range(4)] for row in range(3) ] for depth in range(2)]


# 첫 번째 : 1 번째 Matrix가 반환
# 두 번째 : 2 번쨰 Martix가 반환
for matrix in bar :
    for row in matrix:
        for col in row :
            print(col)
    #     print (row) 
    # print(matrix)
    


for matrix in bar :
    for row in matrix:
        for col in row :
            print(col,"\t",end="")
        print()
    print("-"*10)