import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 7번 문제. 송아지 찾기 (BFS: 상태트리 탐색)

# 내 풀이

# 5번에서 maximum recursion 오류
'''
def DFS(p):
    global cnt
    if p == e:
        print(cnt)
        return
    else:
        cnt += 1
        if e - p > 3:
            DFS(p + 5)
        elif e - p < 0:
            DFS(p - 1)
        else:
            DFS(p + 1)
'''

# 해결
'''
def DFS(p):
    global cnt
    if p == e:
        print(cnt)
        return
    else:
        cnt += 1
        sub = e - p
        if sub > 5:
            cnt += sub // 5 - 1
            DFS(p + (sub // 5) * 5)
        elif sub > 3:
            DFS(p + 5)
        elif sub < 0:
            DFS(p - 1)
        else:
            DFS(p + 1)


if __name__ == "__main__":
    s, e = map(int, input().split())
    cnt = 0

    DFS(s)
'''



# 해설
'''
DFS는 Stack, BFS는 Queue 형식으로 문제를 푼다.
한 노드에서 -1, +1, +5한 노드들로 세 자식노드 생성
ch 리스트를 통해 이미 간 노드를 다시 가지 않도록 방지.
'''


MAX = 10000
ch = [0] * (MAX + 1)                # 체크
dis = [0] * (MAX + 1)               # 거리
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):            # next에 now-1 부터 now + 5 까지 순서대로 대입
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])





