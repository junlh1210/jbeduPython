a = int(input("숫자1 : "))
b = int(input("숫자2 : "))
c = input("원하는 연산(+,-,*,/,//,%,**)은? : ")

if (c == '+'):
    d = a+b
elif (c == '-'):
    d = a-b
elif (c == '*'):
    d = a*b
elif (c == '/'):
    d = a/b
elif (c == '//'):
    d = a//b
elif (c == '%'):
    d = a%b
elif (c == '**'):
    d = a**b
print(f"{a}{c}{b}는 {d}입니다")