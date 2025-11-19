# 1~10까지의 곱

t = 1   # 0으로 하면 곱셈이므로 결과가 항상 0
for i in range(1, 10+1, 1):
    t *= i

print(t)