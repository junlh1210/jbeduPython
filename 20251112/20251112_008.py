# for문에 리스트 직접 입력

score = [90, 25, 67, 45, 80]
number = 0 
for a in score: 
    number = number +1          # index의 역할
    if a >= 60: 
        print(f"{number}번 학생은 합격입니다.")
    else: 
        print(f"{number}번 학생은 불합격입니다.") 