# for -> while

s = 0
for i in range(1, 100+1, 1):
    s = s + i
print(f"1~100까지의 합은 {s}")

print("=" * 30)

s = 0
i = 0
while i<=100:
    s = s + i
    i = i +1
print(f"1~100까지의 합은 {s}")