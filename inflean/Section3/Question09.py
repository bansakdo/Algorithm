import sys

sys.stdin = open("input.txt", "rt")

# 9번 문제. 봉우리

# 내가 푼거
'''
n = int(input())
# 가장자리 0으로 초기화 하면서 입력받음 
matrix = [[0] * (n+2)]
for _ in range(n):
    tmp = [0]
    tmp += [int(x) for x in input().split()]
    tmp.append(0)
    matrix.append(tmp)
matrix += [[0] * (n+2)]

cnt = 0
top = []
for i in range(1, n+1):
    for j in range(1, n+1):
        around = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        around_val = [matrix[i-1][j], matrix[i+1][j], matrix[i][j-1], matrix[i][j+1]]   # 상하좌우 값 
        target = [i, j]                                                                 # 현재 위치
        target_val = matrix[i][j]                                                       # 현재 값
        if top.__contains__(around[0]) or top.__contains__(around[2]):                  # 윗칸과 왼쪽칸이 봉우리면 패스
            continue
        for x in around_val                 # 현재 값과 주변 값들 비교
            if x >= target_val:
                break
        else:
            cnt += 1
            top.append(target)              #  현재 위치가 봉우리이면 top에 현재 위치 추가

print(cnt)
'''


# 해설
dx = [-1, 0, 1, 0]                          # 상하좌우 비교를 위한 리스트
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):    # all은 안이 모두 참이어야 참 리턴
            cnt += 1
print(cnt)


