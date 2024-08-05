"""
# One-dimensional list
# 1 차원 리스트
bar = [50,10,30,40,20]

for item in bar:
    print(item)
print("-"*30)

for index in range(-1,-5,-1):
    print(bar[index])
    
# 원소(Element) 30을 100으로 변경
# bar[좌표] = 100
bar[2] = 100

print(bar)
"""

"""
# 리스트 생성법
# # 리스트 컴프리헨션 (익숙해져야 하는 것)
# bar = [ 0 for _ in range(6)]
# print(bar)

# # or 

# foo = [0] * 6
# print(foo)
"""

"""
bar = [10,20,30,40]
print(bar)

# del bar[index]
del bar[2]
print(bar)

# bar.pop()
bar.pop(2)  # del 과의 차이점은 del은 삭제값을 없애지만 pop은 변수를 지정하고 pop을 쓰는 경우 삭제값이 변수가 되고 그 리스트에 값이 삭제된다.
print(bar)
"""

# pop VS def
while len(bar) > 0 :
    item = bar.pop(0)
    print(item)
