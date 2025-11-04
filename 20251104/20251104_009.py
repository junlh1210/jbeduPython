# 이름과 학번, 두 과목의 점수를 입력 받아서
# 이름과 학번, 총점과 평균을 출력하는 코드 작성

a = input("이름 : ")
b = input("학번 : ")
c = int(input("점수 1 : "))
d = int(input("점수 2 : "))
print(f"이름은 {a}, 학번은 {b}")
print(f"총점 = {c+d}")
print(f"{a} 학생의 평균 = {(c+d)/2}")
