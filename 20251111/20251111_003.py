# 문자열을 다루기
# 리스트 요소 출력

a = [1, 2, 3]
b = "korea seoul"
c = ["korea seoul", 100, 200, "aaa", 300]

print(a)
print(a[0])
print(a[-1])        # 음수인덱스
print(a[0], a[2])
print(a[0]+a[2])

print("="*30)

# 문자열은 리스트처럼 다룰 수 있다
print(b[0])
print(b[0], b[6])
print(b[-1])
print(b[2:5])       # 인덱스: 2, 3, 4

print("="*30)

print(c[0])
print(c[1], c[3])
print(c[-1])
print(c[0:3])       # 인덱스: 0, 1, 2