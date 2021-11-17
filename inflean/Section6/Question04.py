import sys

sys.stdin = open("input.txt", "rt")


# 4번 문제. 합이 같은 부분집합(DFS: 아마존 인터뷰)

# 내 풀이
'''
def DFS(x):
    if x == n + 1:
        return
    else:
        tot = 0
        for i in range(n):
            if ch[i+1] == 1:
                tot += a[i]
        if tot == aim:
            return True

        ch[x] = 1
        flag = DFS(x+1)
        if flag:
            return True
        ch[x] = 0
        flag = DFS(x+1)
        if flag:
            return True

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    aim = sum(a) / 2
    ch = [0]*(n+1)

    res = DFS(1)

    if res:
        print("YES")
    else:
        print("NO")
'''





# 해설

def DFS(L, sum):        # L : Level(depth)
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)         # 프로그램 전체 종료
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")

'''
부분집합의 합을 확인 할 때, total / 2로 할 경우,
total이 홀수이면 다른 결과가 나올 수 있음.
ex) total = 13, {1, 2, 3}이면 부분집합의 합은 6, total/2 = 6.5이므로 다르지만 YES가 될 경우가 있다.
'''
