# 1. 현재 Working Directory
# 2. pythonpath 환경 변수에 명시된 디렉토리
# 3. Built-in Module(표준 라이브러리) 디렉토리
# 4. Third-path 패키지 디렉토리 : site-packages


import sys # 파이썬 인터프리터와 상호작용 기능 제공

# sys.path 변수 자료형 출력
print(type(sys.path)) 

# sys.path 리스트에 각 경로를 출력
for path in sys.path:
    print(path)