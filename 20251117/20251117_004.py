## 기후 데이터 분석 ##

#### 월별 기온 데이터를 이용하여, 최고 기온과 최저 기온을 구하고, 평균 기온을 계산하세요. 
#### 또한, 특정 온도(20도) 이상의 달을 출력하세요.

# 1. 월별 기온 데이터 (섭씨) - 딕셔너리
temperature_data = {
    'M1': -2, 'M2': 0, 'M3': 5, 'M4': 12, 'M5': 18, 'M6': 22,
    'M7': 25, 'M8': 25, 'M9': 20, 'M10': 15, 'M11': 7, 'M12': 2
}

# 2. 최고 기온 구하기
values = temperature_data.values()
print(f"최고 기온 : {max(values)}")

# 3. 최저 기온 구하기
values = temperature_data.values()
print(f"최저 기온 : {min(values)}")

# 4. 평균 기온 구하기
values = temperature_data.values()
print(f"평균 기온 : {sum(values)/len(values):.2f}")


# 5. 기온이 20도 이상인 달만 출력
month20 = []
for k, v in temperature_data.items():
    if v >= 20:
        month20.append(k)
print(f"20도 이상인 달 : {month20}")

# 딕셔너리 컴프리헨션 사용
print(f"20도 이상인 달 : {[k for k, v in temperature_data.items() if v>=20]}")
