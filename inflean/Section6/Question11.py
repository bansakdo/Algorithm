import sys

sys.stdin = open("input.txt", "rt")

# 11번 문제. 수들의 조합
'''
def DFS(L, s):
    global cnt, res
    if L == k:
        sum = 0
        for x in res:
            sum += x
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = nums[i]
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    cnt = 0
    res = [0] * k
    m = int(input())
    DFS(0, 0)
    print(cnt)
'''


# 해설

'''
내가 푼거에서는 마지막에 for문을 사용하지만
해설에서는 DFS 호출때마다 숫자를 더해줌. 시간복잡도가 낮아질 수도 있음.
'''
def DFS(L, s, sum):                 # L: level, s: start, sum: 합계
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])



if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0

    DFS(0, 0, 0)
    print(cnt)


