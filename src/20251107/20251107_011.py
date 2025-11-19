# 숫자 맞추기 게임

ans = 7
for i in range(5):  # (0, 5, 1)과 동일
    num = int(input("숫자를 맞혀보세요 : "))

    if num == ans:
        print("정답입니다!!!")
        break
    else:
        print("틀렸습니다")
print("게임 끝")  