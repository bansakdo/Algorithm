import sys

sys.stdin = open("input.txt")

# 1번 문제. 최대 점수 구하기

# 내 풀이
'''
def DFS(L):
    global tot, q, m
    if L == n:
        print(tot)
        return
    else:
        if m >= q[L][2]:
            m -= q[L][2]
            tot += q[L][1]
        DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    q = []                                      # questions
    for _ in range(n):
        s, t = map(int, input().split())        # score, time
        e = round(s / t, 2)                     # efficiency
        q.append([e, s, t])
    q.sort(reverse=True)
    tot = 0                                     # total score

    DFS(0)
    # print(tot)
'''

# 해설

def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])
        DFS(L, sum, time)




if __name__ =="__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)


