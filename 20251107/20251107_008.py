# 입력받은 부분의 구구단을 출력

dan = int(input("원하는 단? : "))
for i in range(1, 9+1, 1):
    print(f"{dan} * {i} = {dan*i}")