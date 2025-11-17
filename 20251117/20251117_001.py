## 딕셔너리 활용2

## 출석 관리 ##

# 학생 이름과 출석 여부를 저장한 딕셔너리 (True는 출석, False는 결석)
attendance = { '홍길동': True,
               '이순신': False,
               '김유신': True,
               '유관순': True
             }

# 이순신 학생의 출석 상태 조회
print(attendance['이순신'])

# 이순신 학생의 출결상태를 "출석" 또는 "결석"으로 표현

if attendance['이순신']:    # boolean값이면 추가 비교가 필요없다
    print('출석')
else:
    print('결석')

# 새로운 학생 추가 (신사임당, False)
attendance['신사임당'] = False
print(f"전체 학생 출석 상태 : {attendance}")

# 출석한 학생 이름 출력
for x, y in attendance.items():
    if y:
        print(x)