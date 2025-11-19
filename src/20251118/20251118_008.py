# 두 개 숫자의 평균을 구해서, 평균값을 리턴하는 사용자정의함수(avg)를 작성
# 두 개 숫자는 정수로 입력받아 처리한다.


def avg(x, y):
    return (x+y)/2

a = int(input("정수1 : "))
b = int(input("정수2 : "))

print(f"{a}와 {b}의 평균은 {avg(a, b):.0f}입니다")