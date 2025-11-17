# 상품 재고 관리

# 상품과 재고 수량을 저장한 딕셔너리
inventory = {'사과': 30, '바나나': 50, '오렌지': 10}

# 사과의 재고 확인
print(f"사과 재고 : {inventory['사과']}")

# '바나나' 재고 20개 추가 후 변경된 내용 출력
inventory['바나나'] += 20
print(f"바나나 재고 : {inventory['바나나']}")

# 새 상품 추가('포도', 재고 40개) 후 전체 출력
inventory['포도'] = 40
print(f"전체 재고 : {inventory}")

# 각 상품의 재고에서 5개씩 빼기
for k in inventory.keys():
    inventory[k] -= 5
print(f"전체 재고 : {inventory}")