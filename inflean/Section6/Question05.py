import sys

sys.stdin = open("input.txt", "rt")

# 5번 문제. 바둑이 승차(DFS)

# 내 풀이. 5번 입력 시간 오래걸림..
'''
def DFS(x, heaviest):
    print(ch)
    tot = 0
    for i in range(n):              # 이전꺼까지 계산하여 그게 최댓값인지 확인
        if ch[i+1] == 1:
            tot += weight[i]
    if tot > limit:
        return heaviest
    elif tot > heaviest:
        heaviest = tot

    if x == n + 1:                  # 마지막이면 위에서 계산한 값 리턴
        return heaviest
    else:

        ch[x] = 1
        res = DFS(x + 1, heaviest)
        if res > heaviest:
            heaviest = res
        ch[x] = 0
        res = DFS(x + 1, heaviest)
        if res > heaviest:
            heaviest = res

        return heaviest

if __name__ == "__main__":
    limit, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    ch = [0] * (n+1)

    print(DFS(1, 0))
'''

'''
def DFS(L, sum):
    global heaviest

    if L == n:
        return
    elif sum > limit:
        return
    else:
        if sum > heaviest:
            heaviest = sum
            print(heaviest)

        DFS(L + 1, sum)

        if sum + weight[L] < limit:
            DFS(L + 1, sum + weight[L])



if __name__ == "__main__":
    limit, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    heaviest = 0

    DFS(0, 0)
    print(heaviest)
'''

# 해설
'''
함수에서 전역변수를 사용하고 싶다면 global 키워드 사용
함수에서 리스트의 변수에 접근할 때(a[1])는 global 키워드 사용 할 필요는 없지만
a=a+[2] 와 같이 변수 뒤에 등호를 붙이면 지역변수 선언으로 읽힌다.
'''

def DFS(L, sum, tsum):                  # tsum은 여태 확인한 전체 노드의 합(포함 여부 상관 없이)
    global result
    if sum + (total - tsum) < result:   # total - tsum은 아직 판단하지 않은 값들의 합.
        return                          # 이전에 포함한 값 + 아직 판단하지 않들 값들의 합이 result보다 작으면 더이상 할 필요 없음.
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum + a[L], tsum + a[L])
        DFS(L+1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)