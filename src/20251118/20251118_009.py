## 사용자정의함수(rectangle_area)에는, 가로와 세로 값을 전달받아 
## 사각형의 넓이를 구하는 코드

## 사용자정의함수(circle_area)에는, 반지름 값을 전달받아 
## 원의 넓이를 구하는 코드

## 메인 코드에는 메뉴에서 사각형의 넓이 또는 원의 넓이를 선택 
## -> 선택한 메뉴에 따라 호출할 사용자정의함수가 달라진다.

def rectangle_area(x, y):
    return x*y
    
def circle_area(r):
    return r*r*3.14


while True:
    print("=======================")
    print("1. 사각형의 넓이 구하기")
    print("2. 원의 넓이 구하기")
    print("0. 종료")
    print("======================= \n")
    menu=int(input("메뉴번호 선택 : "))
    print()
    
    if(menu==0):
        print("프로그램을 종료합니다")
        break                   
    elif(menu==1):                   
        a = int(input("가로 : "))
        b = int(input("세로 : "))
        print(f"가로 {a},  세로 {b} 인 사각형의 넓이 = {rectangle_area(a, b)}")
        print("")                   
    elif (menu==2):                   
        a = int(input("반지름 : "))
        print(f"반지름 {a} 인 원의 넓이 = {circle_area(a)}")
        print("")
    else:
        print("1 혹은 2를 입력해 주세요")