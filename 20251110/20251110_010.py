# 총점과 평균을 계산하여 출력한다
# 처리할 학생 수는 직접 입력받아, 입력받은 학생 수 만큼 처리한다
# 모든 학생들은 세 과목의 점수를 각각 입력받아 성적을 처리한다.

n = int(input("학생 수 : "))

for i in range(1, n+1, 1):
    korean = int(input(f"{i}번째 학생 국어점수 : "))
    math = int(input(f"{i}번째 학생 수학점수 : "))
    english = int(input(f"{i}번째 학생 영어점수 : "))

    total = korean + math + english
    avg = total / 3.0

    print(f"{i}번째 학생의 총점은 {total}이고 평균은 {avg:.2f}입니다")
    print()
print("="*10,"작업 완료", "="*10)