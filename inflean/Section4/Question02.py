import sys

sys.stdin = open("input.txt", "rt")

# 랜선자르기(결정알고리즘)


# 내가 푼거 -> 실패

'''
k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))
    
tot = sum(a)
m = tot // n
while True:
    print("----")
    i = 0                           # 만들어진 랜선 개수
    largest_rest = 0                # 나머지가 가장 큰 값
    whole = 0                       # 나머지가 가장 클 때 원래의 랜선의 길이
    for x in a:
        i += (x // m)               # 만들어진 랜선을 더함
        rest = x % m                # 만들고 남은 랜선
        if rest > largest_rest:
            largest_rest = rest
            whole = x

        print()
        print(i)
        print(rest)
        print(x)
        print(m)
        print(largest_rest)
    else:
        if i >= n:                  # 만들어진 랜선의 개수가 원하는 개수 이상일 때
            break
        else:                       # 랜선을 원하는 만큼 못 만들었을 때
            # 나머지가 가장 크게 남은 랜선에서 1개 더 만들수 있는 길이로 길이 조정
            m = (whole // ((whole // m) + 1))
print(m)
'''


# 강의 설명 들은 후
'''
k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))
s = 0
e = max(a)
res = 0

while True:
    val = 0
    mid = s + (e - s) // 2          # 중간값
    for x in a:                     # 개수
        val += x // mid
    if val >= n:
        s = mid + 1
    elif val < n:
        e = mid - 1
    if s >= e:
        res = e
        break
print(res)
# '''


# 해설
'''
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):                      # 입력
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
'''