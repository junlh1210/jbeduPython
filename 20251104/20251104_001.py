a = 3
b = 5
print("a의 값은 ==> ",a, "이고, b의 값은 ",b,"입니다.")
print("a의 값은 ==> %.2f 이고, b의 값은 %d 입니다" %(a, b))  # %연산자 포맷팅
print('a의 값은 ==> {} 이고, b의 값은 {} 입니다.'.format(a,b))   # .format()사용 포맷팅
print('a의 값은 ==> {1} 이고, b의 값은 {0} 입니다.'.format(a,b))
print(f"a의 값은 ==> {a}이고, b의 값은 {b}입니다.")  # f-string 포맷
print(f"a+b의 값은 ==> {a+b}이고, a*b의 값은 {a*b}입니다.") # f-string 포맷