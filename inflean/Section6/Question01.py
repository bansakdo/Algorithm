import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 1번 문제. 재귀함수를 이용한 이진수 출력

# 내 풀이
'''
n = int(input())
res = ""

while n > 0:
    res = str(n % 2) + res
    n = n // 2

print(res)
'''

# 해설

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end=' ')

if __name__ == "__main__":
    n = int(input())
    DFS(n)

'''
백트래킹 : 함수에서 리턴하여 함수가 호출된 위치로 돌아오는것 
'''


