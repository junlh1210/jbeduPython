a = int(input("숫자1 : "))
b = int(input("숫자2 : "))
c = input("원하는 연산(+,-,*,/,//,%,**)은? : ")

if (c == '+'):
    print(f"{a}{c}{b}는 {a+b}입니다")
elif (c == '-'):
    print(f"{a}{c}{b}는 {a-b}입니다")
elif (c == '*'):
    print(f"{a}{c}{b}는 {a*b}입니다")
elif (c == '/'):
    print(f"{a}{c}{b}는 {a/b}입니다")
elif (c == '//'):
    print(f"{a}{c}{b}는 {a//b}입니다")
elif (c == '%'):
    print(f"{a}{c}{b}는 {a%b}입니다")
elif (c == '**'):
    print(f"{a}{c}{b}는 {a**b}입니다")