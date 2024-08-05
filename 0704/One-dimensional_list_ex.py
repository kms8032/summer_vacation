# 리스트 생성
my_list = [10,20,30,40,50]
print("Initial list:", my_list)     # Initial list: [10, 20, 30, 40, 50]

# 리스트의 특정 요소 접근
print("Element at index 2:",my_list[2])     # Element at index 2: 30

# 전체 리스트 출력
print("Full list:", my_list)        # Full list: [10, 20, 30, 40, 50]

# 리스트의 특정 요소 업데이트
my_list[1] = 25
print("Update list:",my_list)       # Update list: [10, 25, 30, 40, 50]

# 리스트에 요소 추가
my_list.append(60)
print("List after addin elemnet:",my_list)      # List after addin elemnet: [10, 25, 30, 40, 50, 60]

# 리스트 내 요소를 지정된 위치에 삽입
my_list.insert(2,15)
print("List after inserting element at index 2:",my_list)   # List after inserting element at index 2: [10, 25, 15, 30, 40, 50, 60]


