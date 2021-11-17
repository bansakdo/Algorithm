import sys

sys.stdin = open("input.txt", "rt")

# 7번 문제. 동전교환

# 내 풀이
'''
def DFS(L, cnt):
    global m, smallest
    if L == n:
        if m == 0 and cnt < smallest:
            smallest = cnt
            print(a)
        return
    else:
        # 3번만 틀림
        cnt += (m // types[L])
        a.append([types[L], m // types[L]])
        m %= types[L]
        if m > 0:
            DFS(L+1)
        
if __name__ == "__main__":
    n = int(input())
    types = list(map(int, input().split()))
    m = int(input())
    smallest = 2147000000
    a = []

    types.sort(reverse=True)

    DFS(0, 0)
    print(smallest)
'''

'''

        for x in range((m // types[L]) + 1):
            cnt += x
            m -= (types[L] * x)
            if m == 0:
                if cnt < smallest:
                    smallest = cnt
                m += (types[L] * x)
                return
            tmp = 0
            for i in range(L + 1, n):
                tmp += (m // types[i])
            print("tmp + cnt :", tmp+cnt)
            print("smallest:", smallest)
            if tmp + cnt < smallest:
                DFS(L + 1, cnt)
            m += (types[L] * x)
            cnt -= x
'''

'''
def DFS(L, sum):
    global m, smallest
    if sum == m:
        if L < smallest:
            smallest = L
    elif sum > m:
        return
    else:

        for i in range(n):
            DFS(L+1, sum + types[i])
        # cnt += (m // types[L])
        # a.append([types[L], m // types[L]])
        # m %= types[L]
        # if m > 0:
        #     DFS(L + 1)


if __name__ == "__main__":
    n = int(input())
    types = list(map(int, input().split()))
    m = int(input())
    smallest = 2147000000
    a = []

    types.sort(reverse=True)

    DFS(0, 0)
    print(smallest)
'''



# 해설
'''
한 부모노드에서 동전의 종류만큼의 자식노드 생성.
level의 수가 사용된 동전의 개수
'''

def DFS(L, sum):
    global res
    if L >= res:                    # res는 L의 최솟값이고,
        return                      # L이 res보다 크면 더이상 연산할 필요가 없음.
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)

    DFS(0, 0)
    print(res)
