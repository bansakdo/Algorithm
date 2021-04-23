# 최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')           # 파이썬에서 지원하는 가장 큰 값 저장

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print("최솟값: ",arrMin)


for x in arr:
    if x < arrMin:
        arrMin = x
print("최솟값: ", arrMin)

print("최솟값: ", min(arr))