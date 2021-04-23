import sys


sys.stdin = open("input.txt", "rt")

# 5번 문제. 최대 선 연결하기

# 내 풀이
'''
def DFS(lv, r, line):          # 왼쪽, 오른쪽, 선 개수
    global res, tt
    if lv == n:
        tt = max(tt, line)
    else:
        l = l_arr[lv]
        ri = r_arr.index(l)
        if ri > r:
            DFS(lv + 1, ri, line + 1)
        DFS(lv + 1, r, line)


if __name__ == "__main__":
    n = int(input())
    r_arr = [int(x) for x in input().split()]
    l_arr = [int(x) for x in range(1, n+1)]
    res = []
    tt = 0

    DFS(0, 0, 0)
    print(tt)
'''


# 해설

n = int(input())
arr = [int(x) for x in input().split()]
arr.insert(0, 0)
res = [0] * (n+1)
res[1] = 1
cnt = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and res[j] > max:
            max = res[j]
    res[i] = max + 1
    if res[i] > cnt:
        cnt = res[i]
print(cnt)



