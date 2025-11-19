## 사용자정의 함수 "gugudan"을 만든다.
## gugudan 함수에서는 '단'을 매개변수로 전달받아서, 
## 해당 단을 출력하는 내용이 정의되어 있다.

## gugudan을 호출할 때는 출력을 원하는 '단'을 인자로 전달한다.

def gugudan(x):
    for i in range(1, 9+1, 1):
        print(f"{x} x {i} = {x*i}")

num = int(input("원하는 단 : "))
gugudan(num)