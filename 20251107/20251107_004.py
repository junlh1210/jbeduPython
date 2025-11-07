# 1~100까지 홀수, 짝수의 합을 구하시오

t_odd = 0
t_even = 0

for a in range(1, 100+1, 1):
    if a%2 == 0 :
        t_even += a
    else:
        t_odd += a

print(f"1~100까지 홀수의 합 : {t_odd}")
print(f"1~100까지 짝수의 합 : {t_even}")