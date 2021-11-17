import sys

sys.stdin = open("input.txt", "rt")

# 2번 문제. K번째 수

# 내가 푼거
'''
t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())

    list = [int(x) for x in input().split()]
    list = list[s-1:e]              # 문제는 순서가 1부터 시작하고 index는 0부터 시작하므로.
    list.sort()
    print("#{i} ", list[k-1])
'''

# 해설
T = int(input())
for t in range(T):
    n, s, e, k =  map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))



