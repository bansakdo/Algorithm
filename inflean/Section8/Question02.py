import sys

sys.stdin = open("input.txt", "rt")


# 2번 문제. 네트워크 선 자르기(Top-down, 재귀)

# 내 풀이
'''
def DFS(l, a, b):
    global cnt
    if l == 0:
        cnt += 1
        return 1
    elif l < 0:
        return 0
    else:
        if l not in mem.keys():
            v1 = DFS(l - 1, a + 1, b)
            v2 = DFS(l - 2, a, b + 1)
            v = v1 + v2
            mem[l] = v
        else:
            v = mem[l]
            cnt += v
        return v

if __name__ == "__main__":
    n = int(input())
    cnt = 0
    mem = dict()
    DFS(n, 0, 0)
    print(cnt)
'''


# 해설


def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))





