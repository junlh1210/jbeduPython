## 입력받은 인원수만큼 점수를 입력받아,
## 리스트에 점수를 추가하는 코드 작성

## 위코드에 다음 내용을 추가
## [추가조건]80점 인상인 인원수와
##          80점 미만인 인원수를 구하여 각각 출력하고,
##          전체 데이터 개수를 출력 

## 1개의 for문으로 작성할 것

num = int(input("인원수 : "))

list1 = []
good, bad = 0, 0        # 초기화를 한번에
for i in range(1, num+1, 1):
    x = int(input(f"{i}번 점수 : "))
    list1.append(x)
    if x>=80:
        good += 1
    else:
        bad += 1
print(f"80점이상 인원수 : {good}")
print(f"80점미만 인원수 : {bad}")
print(f"전체 데이터의 갯수 : {len(list1)}")