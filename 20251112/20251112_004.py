# renage함수와 print문의 sep

list1 = []

for i in range(10,50,10):           # 50은 입력되지 않는다
    list1.append(i)
print(list1)

print()

for i in [10,20,30,40,50,60,70]:    # for문에 리스트 직접사용
    print("파이썬",i, sep="====")   # 구분자가 ====