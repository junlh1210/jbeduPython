# 165페이지

import datetime

now=datetime.datetime.now()
print(f"{now}\n")

print(now.year,"년")    # xxxx
print(now.month,"월")   # 01~12
print(now.day,"일")     # 01~31
print(now.hour,"시")    # 00 ~ 23
print(now.minute,"분")  # 00~59
print(now.second,"초")  # 00~59

print()
if (now.hour > 12):
    print(f"현재 시각은 {now.hour}시로, 오후입니다")
else:
    print(f"현재 시각은 {now.hour}시로, 오전입니다")