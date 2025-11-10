# 하나의 정수를 입력받아,
# 1부터 입력받은 숫자까지의 합을 구하는 코드

n = int(input("정수 : "))

s = 0
for i in range(1, n+1, 1):
    s += i
print(f"1부터 {n}까지의 합은 {s}")

print("=" * 30)

s = 0
i = 1
while i<= n:
    s += i
    i += 1
print(f"1부터 {n}까지의 합은 {s}")