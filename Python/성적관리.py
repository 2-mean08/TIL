#3명의 학생의 성명, 국어, 영어, 수학 점수를 입력 받아 각 학생별 합, 총점을 출력하고 맨 마지막 줄에 과목별 합, 평균, 전체학생 평균을 출력

# 학생 정보를 저장할 리스트 초기화
list1= []
list2= []
# 3명의 학생 정보 입력 받기
for i in range(3):
    list1.append(input("이름: "))
    list1.append(int(input("국어성적: ")))
    list1.append(int(input("수학성적: ")))
    list1.append(int(input("영어성적: ")))
    list2.append(list1) #입력 받은 성적 정보를 리스트2에 저장
    list1 = [] #다음 학생정보를 받기 위해 리스트 비우기

# 과목별 합계 및 평균 계산
kor_sum = sum(student[1] for student in list2)  # 국어 총점
math_sum = sum(student[2] for student in list2)  # 수학 총점
eng_sum = sum(student[3] for student in list2)  # 영어 총점

kor_avg = kor_sum / 3  # 국어 평균
math_avg = math_sum / 3  # 수학 평균
eng_avg = eng_sum / 3  # 영어 평균

# 전체 학생 총합 및 평균 계산
total_sum = kor_sum + math_sum + eng_sum  # 전체 합계
total_avg = total_sum / (3 * 3)  # 전체 평균 (총 점수 / 총 과목 수)

# 특정 학생의 성적 수정 기능
def modify_score(student_name, subject_index, new_score):
    for student in list2:
        if student[0] == student_name:  # 이름으로 학생 찾기
            student[subject_index] = new_score  # 과목 점수 수정
            print(f"\n{student_name}의 {['국어', '수학', '영어'][subject_index - 1]} 점수가 {new_score}로 변경되었습니다.")
            return
    print(f"\n{student_name} 학생을 찾을 수 없습니다.")

#학생별 과목별 점수와 평균 및 합계 출력
def print_all_students():
    for i in range(3):
        print("\n%d번째 학생" %(i+1))
        print("%s" %list2[i][0], end = " ")
        hap = 0
        for j in range(1,4,1):
            print("%d"%list2[i][j], end = " ")
            hap += list2[i][j]
        print("--> 합: %3d, 평균: %3.1f \n" %(hap, hap/3))
    # 과목별 합계 및 평균 출력
    print("\n과목별 합계 및 평균")
    print("국어: 합계 = %d, 평균 = %.1f" % (kor_sum, kor_avg))
    print("수학: 합계 = %d, 평균 = %.1f" % (math_sum, math_avg))
    print("영어: 합계 = %d, 평균 = %.1f" % (eng_sum, eng_avg))

    # 전체 학생 총합 및 평균 출력
    print("\n전체 학생 총합 및 전체 평균")
    print("전체 합계: %d" % total_sum)
    print("전체 평균: %.1f" % total_avg)


#실행할 메뉴 선택
while True:
    print("1.전체 학생 출력")
    print("2. 특정 학생 성적 변경")
    print("3. 종료")

    choice = input()

    if choice == "1":
        print_all_students()
    elif choice == "2":
        student_name = input("\n성적을 수정할 학생 이름을 입력하세요: ")
        subject = input("수정할 과목을 입력하세요 (국어/수학/영어): ")
        new_score = int(input("새로운 점수를 입력하세요: "))
        
        # 과목 인덱스 설정 (국어: 1, 수학: 2, 영어: 3)
        subject_index = {"국어": 1, "수학": 2, "영어": 3}.get(subject)
        if subject_index:
            modify_score(student_name, subject_index, new_score)
        else:
            print("\n잘못된 과목명이 입력되었습니다.")
    elif choice == "3":
        print("\n프로그램을 종료합니다.")
        break
    else:
        print("\n잘못된 입력입니다. 다시 선택하세요.")
            
