# 리스트 컴프리핸션

list1 =[ ["홍길동", 100],
         ["김길동", 95],
         ["이길동", 88]   ]

for i in list1:
    print(i[0])
    print(i[1])

print("="*20)

for x, y in list1:      # 리스트 요소가 분해되어 각각 x, y에 저장된다
    print(x)
    print(y)