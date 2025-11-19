# 1~100까지 3의배수와 5의배수의 합을 구하는 코드
# for문은 1개만 사용

total_3 = 0
total_5 = 0

for i in range(1, 100+1, 1):
    if (i%3 == 0):
        total_3 += i
    if (i%5 == 0):  # elif를 사용하면 3, 5의 공배수가 제외된다
        total_5 += i

print(f"3의 배수의 합 : {total_3}")
print(f"5의 배수의 합 : {total_5}")