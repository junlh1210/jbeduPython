# 비교연산자
x=6
y=2
print(x==y) # False
print(x>y)  # True
print(x<y)  # False
print(x>=y) # True
print(x<=y) # False
print(x!=y) # True

# 연산자 우선순위 (산술연산자가 비교연산자보다 우선)
print(2 > 1 + 1)        # False 
print(7 // 3 == 2)      # True
print(1 + 2 + 3 <= 6)   # True
print(6 % 2 == 0)       # True

# 논리 연산자
x=90
y=83
print(x>=85 or y>=85)   # True
print(x>=85 and y>=85)  # False