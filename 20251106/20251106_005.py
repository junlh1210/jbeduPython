## 세과목 점수를 입력받아서,
## 평균이 80점 이상이면 "우수"를 출력
## 70점 이상이면 "양호"를 출력
## 나머지는 "미흡"을 출력하는 코드 작성

sco1 = int(input("국어 : "))
sco2 = int(input("영어 : "))
sco3 = int(input("수학 : "))

avg = (sco1 + sco2 + sco3)/ 3

if avg >= 80: 
    rating = "우수"
elif avg >= 70:
    rating = "양호"
else:
    rating = "미흡"

print(f"평균점수는 {avg:.2f}점, 평가 : {rating}")