# 사용자 정의 함수

def fadd(n, m):
    s = n + m
    print(f"{n} + {m} = {s}")
    
a=3
b=4
fadd(a,b)
fadd(a+10, b-2)
fadd(10, 2, a)       # 에러 발생