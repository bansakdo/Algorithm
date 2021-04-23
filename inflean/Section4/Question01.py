import sys

sys.stdin = open("input.txt", "rt")

# 1번 문제. 이분검색

# '''
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 정렬 (선택정렬)
for i in range(n):
    minimum = sys.maxsize                   # 시스템에서 지원하는 최대 값
    idx = i                             # 현재 위치
    for j in range(i+1, n):             # i 뒤에서 가장 작은 값 찾음
        if a[j] < minimum:
            minimum = a[j]
            idx = j
    else:
        if a[idx] < a[i]:               # 뒤에서 찾는 가작 작은 값이 a[i]보다 작으면 갑 교환
            a[i], a[idx] = a[idx], a[i]

# 이분검색                  # log(n)번만에 찾음.
s = 0                               # 시작 인덱스
e = n - 1                           # 끝 인덱스
while True:
    half = s + ((e - s) // 2)       # 중간 인덱스 (기준 인덱스)
    aim = a[half]                   # 중간 값
    if m == aim:                    # 현재 인덱스가 가리키는 값과 목표값이 같은 경우
        print(half + 1)             # 인덱스이기 때문에 +1
        break
    elif m < aim:                   # 목표값이 현대 가리키는 값보다 작으면 끝 인덱스 변경
        e = half
    elif m > aim:                   # 목표값이 현대 가리키는 값보다 크면 시작 인덱스 변경
        s = half
    if abs(e - s) <= 1 :            # 시작인덱스와 끝 인덱스가 붙어있으면 종료
        print("end!!!")
        break
# '''


# 해설
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1



