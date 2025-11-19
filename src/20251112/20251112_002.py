# 리스트 다루기 (append, del)
# print문의 end : 가장 마지막에 실행
# print문의 sep : 요소 사이에 출력 문자 변경(기본값은 공백문자)

list1 = []
list2 = ['a', 'b', 'c']
list3 = [ 1, 'a', "abc", [1, 2, 3]]

list1.append(1)             # 리스트의 가장 마지막에 추가
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print(list1)

list2.append(11)
print(list2)

del list3[3]                # 인덱스 3번 요소를 지움
print(list3, end="\n\n")    # list3를 출력한후 end를 실행