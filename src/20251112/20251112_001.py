# 리스트에 사용할 수 있는 함수

a = [1, 2, 3]
a.append(11)    # 가장 마지막에 11 추가
print(a)

del a[1]        # 지정된 요소 지우기
print(a)

del a[1:]       # 1부터 끝까지 지우기
print(a)

a.append(20)
a.append(50)
a.append(20)
print(a)        # [1, 20, 50, 20]
a.append(20)

a.remove(20)    # 지정한 값을 검색하여 일치하는 최초 요소를 지운다
print(a)

b=len(a)        # length
print(b)

a.insert(1,10)  # 지정한 자리에 지정한 값 추가
print(a)