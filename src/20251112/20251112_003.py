# for문을 이용하여 list 출력
# print문에 \t는 탭이 입력된다

list3 = [ 1, 'a', "abc", [1, 2, 3]]
for i in range (len(list3)):        # list3의 갯수
    print(f"파이썬\t {i}")
    
print("="*15)

for i in list3:                     # list3 요소가 차례로 입력된다
    print (i)