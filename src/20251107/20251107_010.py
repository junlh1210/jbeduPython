# 반복문 멈추기 : break

total = 0
for i in range(1, 10+1, 1):
    total += i
    print(f"{i}까지의 합 : {total}")
    if total>30:
        print("합이 30이 넘었습니다")
        break