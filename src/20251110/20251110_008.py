n = 0
while True:
    pw = input("비밀번호 : ")
    if (pw == "1234abcd"):
        print("LogIn Pass!!")
        break
    else:
        n += 1
        print(f"{n}회 오류!!!")
        if n==3:
            print(f"5분후에 다시 이용해 주세요")
            break
        else:
            continue
print("="*30)