import sys
import time

sys.stdin = open("input.txt", "rt")
start = time.time()

# 3번 문제. 양팔저울 (DFS)

# 내 풀이
'''
def DFS(water, L, R):
    if water > max:
        return
    else:
        # DFS(water, L, R)
        for i in range(k):
            if ch[i] == 0:
                ch[i] = 1
                DFS(water, L + weights[i], R)
                DFS
  '''

'''
def DFS(d, water, L, R):
    global cnt
    print("\n",res)
    print(d, water, L, R)
    print(ch)
    if water > max_num or L > max_num or R > max_num :
        print("return", max_num, water, L, R)
        return
    elif L == R and res[water] == 0:
        print("equal", water)
        res[water] = 1
        cnt -= 1
    if R != 0 and res[R] == 0:
        print("RR", R)
        res[R] = 1
        cnt -= 1
    if res[water] == 0:
        if water in weights:
            print("contain", water)
            res[water] = 1
            cnt -= 1
        else:
            tmp = 0
            sub = L - R
            for i in range(k):
                if ch[i] == 0:
                    tmp += weights[i]
                    if tmp >= sub:
                        break
            else:
                return

            for i in range(k):
                if ch[i] == 0:
                    ch[i] = 1
                    DFS(d + 1, water, L + weights[i], R)
                    DFS(d + 1, water, L, R + weights[i])
                    ch[i] = 0
    if d == 1:
        for i in range(1, max_num):
            if res[water + i] == 0:
                DFS(d + 1, water + i, water + i, R)


if __name__ == "__main__":
    k = int(input())
    weights = list(map(int, input().split()))
    max_num = sum(weights)
    res = [0] * (max_num + 1)
    ch = [0] * k
    cnt = max_num

    DFS(1, 1, 1, 0)
    print(cnt)



print("time :", time.time() - start)
'''



# 해설
'''
DFS에서 레벨 하나당 무게추 1개씩 재고, 자식노드는 3개씩 필요.
무게가 n인 추를 왼쪽으로 놓으면 +n, 오른쪽으로 놓으면 -n, 둘다 놓지 않으면 0
반복 하다보면 겹치는 경우가 있음. 따라서 겹치는 경우를 방지하기 위해서, 물그릇의 무게가 -가 되면 측정 X
'''

def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)

    else:
        DFS(L + 1, sum + G[L])                  # 추 왼쪽
        DFS(L + 1, sum - G[L])                  # 추 오른쪽
        DFS(L + 1, sum)                         # 추 X



if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))         # 추
    s = sum(G)                                  # 측정 가능한 무게
    res = set()                                 # set 쓴 이유는 중복을 방지하기 위해
    DFS(0, 0)
    print(s - len(res))