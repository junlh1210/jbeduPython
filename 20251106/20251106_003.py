## 현재 시스템에서 날짜와 시간을 알아내고,
## '월'이 3~5사이면 "이번 달은 { }월로, 봄입니다."를,
## '월'이 6~8 사이면 "이번 달은 { }월로, 여름입니다."를,
## '월'이 9~11 사이면 "이번 달은 { }월로, 가을입니다."를,
## '월'이 12월 또는 1~2 사이면 "이번 달은 { }월로, 겨울입니다."를 출력하는 코드 작성

from datetime import datetime

# 시스템의 현재 날짜
now = datetime.now()

if (now.month ==3 or now.month==4 or now.month==5):
    season = "봄"
elif (now.month ==6 or now.month==7 or now.month==8):
    season = "여름"
elif (now.month ==9 or now.month==10 or now.month==11):
    season = "가을"
elif (now.month ==12 or now.month==1 or now.month==2):
    season = "겨울"
print(f"이번 달은 {now.month}월로, {season}입니다")