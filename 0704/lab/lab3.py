# 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력하는 프로그램을 함수를 이용하여 작성
# 함수 구성은 자유
# 학생성적 관리 테이블 구조 예 -> 리스트를 이용하여 구성
# 학생 성적 입력
def student_score():
    num = int(input("학번을 입력하세요.: "))
    name = input("이름을 입력하세요.: ")
    kor = int(input("국어 점수를 입력하세요.: "))
    eng = int(input("영어 점수를 입력하세요.: "))
    math = int(input("수학 점수를 입력하세요.: "))
    sum = kor + eng + math
    avg = sum/3
    student_list = [num,name,kor,eng,math,sum,avg]
    std_score_list.append(student_list)
    
# 학생 목록 출력(입력순)
def std_list_print():
    if std_score_list == []:
        print("아직 입력값이 없습니다.")
    else :
        for i in range(len(std_score_list)):
            print(f'학번: {std_score_list[i][0]} 이름 : {std_score_list[i][1]} 국어: {std_score_list[i][2]} 영어 : {std_score_list[i][3]} 수학 : {std_score_list[i][4]} 총합 : {std_score_list[i][5]} 평균 : {std_score_list[i][6]} ')

# 전체 학생 평균 값
def all_score_avg():
    if len(std_score_list) >= 1 :
        all_avg = 0
        for i in range(len(std_score_list)):
            all_avg += std_score_list[i][6]
        
        return all_avg//len(std_score_list)
    else :
        return 0     
std_score_list = []

# 루프 설정
while True :
    print("-"*20)
    print("1. 학생 성적 입력: ")
    print("2. 학생 목록 출력(입력순): ")
    print("3. 프로그램 종료: ")
    # 현 입력데이터 갯수 출력
    print(f"\n현 입력데이터 갯수 :{len(std_score_list)}")
    # 전체 학생 평균 값 출력
    print(f"전체 학생 평균 값: {all_score_avg()} ")
    select = int(input("메뉴를 선택하세요."))
    if select == 1 :
        student_score()
    elif select == 2 :
        std_list_print()
    # 프로그램 종료
    elif select == 3:
        print("프로그램을 종료합니다.")
        break
    else :
        print("옳지않은 입력값입니다. 다시 입력해주세요.")
    


