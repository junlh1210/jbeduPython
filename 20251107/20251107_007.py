# 정수 하나를 입력받아서,
# 1부터 입력받은 정수까지 합을 구하는 코드

a = int(input("정수 : "))
t = 0

for i in range(1, a+1, 1):
    t += i

print(f"1부터 {a}까지 합 : {t}")